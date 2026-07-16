import logging
import os
import signal
import sys
import json
import argparse
import traceback
import warnings
import lightning
import re
import r4a_utils
import tts.lang_list as lang_list # https://raw.githubusercontent.com/facebookresearch/seamless_communication/main/demo/m4tv2/lang_list.py
import pprint
import time
from gpt4all import GPT4All
from langcodes import Language
import redis
import diart.operators as dops
import numpy as np
import rich
import rx.operators as ops
from rx.scheduler import ThreadPoolScheduler
from threading import current_thread
import whisper_timestamped as whisper
import faster_whisper
from faster_whisper import WhisperModel
from diart import SpeakerDiarization, SpeakerDiarizationConfig, blocks
from diart.sources import MicrophoneAudioSource
from pyannote.core import Annotation, SlidingWindowFeature, SlidingWindow, Segment
import openai
import signal
import streamlit as st
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer, SeamlessM4TModel, AutoProcessor 
from deep_translator import GoogleTranslator, single_detection
from huggingface_hub import login
import time
import csv
import datetime
import soundfile as sf
import glob

r4a_utils.add_to_syspath('tts', '.') # needed to ensure that modules are found

# import torch # uncomment once GPU is supported
from tts.coqui_tts import CoquiSpeaker
from tts.bark_tts import BarkSpeaker
from tts.espeakng_tts import EspeakngSpeaker
from tts.seamless_tts import SeamlessSpeaker

# This code base has been modified from: https://gist.github.com/juanmc2005/ed6413e697e176cb36a149d8c40a3a5b

# Set global vars /config
end_program = False
scheduler = ThreadPoolScheduler(1)
speaker = None
redis_client = redis.Redis(host='localhost', port=6379, db=0)
error_emojis = " 🚫❌⚠️ "
supported_tr_models =  ["facebook/hf-seamless-m4t-medium", "facebook/m2m100_418M"]
benchmark_speakers = []

# parse config
with open ('r4a_config.json', 'r') as config_file:
    r4a_config = json.load(config_file)

# parse cli args
desired_width = 100 # number of characters of help text to print in column
parser=argparse.ArgumentParser(description="This program take microphone input and translates between" \
        " multiple speakers or privdes a response from a chatbot") #, 
        #formatter_class=lambda prog: argparse.HelpFormatter(prog, 
        #    max_help_position=desired_width, width=desired_width))

for key in r4a_config.keys():
    value = r4a_config[key]['value']
    desc = r4a_config[key]['desc']
    if type(value) == bool:
        parser.add_argument(f"--{key}", help=f"{desc} (default: {value})", action="store_true", default=value)
    else:
        if key.upper().endswith("_KEY"):
            parser.add_argument(f"--{key}", help=f"{desc} (default: YOUR KEY - REDACTED)", default=value)
        else:
            parser.add_argument(f"--{key}", help=f"{desc} (default: {value})", default=value)

args = parser.parse_args()

# Suppress whisper-timestamped warnings for a clean output
logging.getLogger("whisper_timestamped").setLevel(logging.ERROR)

# https://lightning.ai/docs/pytorch/stable/extensions/logging.html#automatic-logging
# configure logging at the root level of Lightning
logging.getLogger("lightning.pytorch").setLevel(logging.ERROR)

log_level = getattr(logging, args.log_level.upper(), None)

if not isinstance(log_level, int):
    raise ValueError(f"Invalid log level: {log_level}")

r4a_logger = logging.getLogger(__name__)
r4a_logger.setLevel(log_level)
if not args.benchmark_only:
    sound_device = r4a_utils.get_sound_device(logger=r4a_logger)
    r4a_logger.debug(f"After initialization: Sound device is: {sound_device}")

args_dict = vars(args)

for arg_key in args_dict.keys():
    if arg_key.upper().endswith("KEY"):
        r4a_logger.debug(f"Setting {arg_key} to value of environment variable, or falling back to config value")
        real_value = os.getenv(args_dict[arg_key], args_dict[arg_key])
        setattr(args, arg_key, real_value)
        r4a_logger.debug(f"Args {arg_key} = KEY_VALUE_REDACTED")
    else:
        r4a_logger.debug(f"Args {arg_key} = {args_dict[arg_key]}")

if args.nogpt:
    args.gpt = False

if args.gpt:
    r4a_logger.debug( "Loading GPT model")
    gpt_model = GPT4All(args.gpt4all_model)

if args.tts:
    if (not args.gpt) and (not args.benchmark_only):
        r4a_logger.warn("You cannot use text to speech without setting benchmark or gpt in the config or on CLI")
        args.tts = False

# see https://github.com/pyannote/pyannote-audio/issues/1576
warnings.filterwarnings("ignore") 
SUPPORTED_TRANSLATORS = ["Facebook", "Google"]
r4a_logger.debug("Finished variable initialization")

def signal_handler(signum, frame):
    global end_program
    r4a_logger.debug("Setting end_program to True")
    end_program = True
    r4a_utils.mute_audio_input_devices(mute=False, logger=r4a_logger) #unmute mic
    sys.exit(0)

def handle_audio_stream(audio_stream, disposable):
    try: 
        while not end_program:
            r4a_logger.info("Starting translation and captioning, begin speaking...")
            audio_stream.read()
    finally:
        r4a_logger.debug("Closing audio stream")
        audio_stream.close()
        disposable.dispose()

def process_audio_files(audio_dir, respond=False):
    if audio_dir.lower().startswith('http'):
        # The files are hosted remotely, download them locally first
        local_base_dir = "/tmp/audio_files"
        r4a_utils.create_local_directory(local_base_dir)
        download_directory(audio_dir, local_base_dir)
        audio_dir = local_base_dir

    audio_files = glob.glob(os.path.join(audio_dir, "*.wav"))  # Adjust the pattern if your audio files have a different extension
    transcriber = WhisperTranscriber(model=args.stt_model)
    for audio_file in audio_files:
        r4a_logger.debug(f"Processing audio file: {audio_file}")
        audio_data, sample_rate = sf.read(audio_file)
        waveform = SlidingWindowFeature(audio_data, SlidingWindow(start=0, duration=1/sample_rate, step=1/sample_rate))
        start_time = time.time()
        transcription = transcriber.transcribe_faster(waveform, start_time) if args.whisper_type == 'faster' else transcriber.transcribe_tstamp(waveform, start_time)
        speaker_transcriptions = transcriber.identify_speakers(transcription, None, 0)  # Assuming no diarization for pre-recorded audio
        if respond:
            respond_and_print(colorize_transcription(speaker_transcriptions))

def benchmark_tts_trn(tts_language_input_json_file=None):
    text_sizes = ['small', 'medium', 'large']
    tts_engines = ["espeakng", "coqui", "seamless", "bark"]
    if args.speakers:
        tts_engines = args.speakers.split(',')
    benchmark_languages = None
    
    # parse languages json file
    if tts_language_input_json_file is None:
        r4a_logger.debug("Setting json file to tts/languages.json")
        tts_language_input_json_file = 'tts/languages.json'

    with open (tts_language_input_json_file, 'r') as language_file:
        r4a_logger.debug("parsing language file")
        benchmark_languages = json.load(language_file)

    for tts_engine in tts_engines:
        r4a_logger.debug(f"Creating speaker for {tts_engine}")
        tts_speaker = None
        if args.tts:
            tts_speaker = create_speaker(tts_engine=tts_engine)
        for lang in benchmark_languages:
            output_text_sizes = benchmark_languages[lang]
            if args.tts:
                r4a_logger.debug(f"Changing voice of {tts_engine} speaker to {lang}")
                if is_supported_voice(lang):
                    tts_speaker.voice = lang
            for text_size in text_sizes:
                text_to_speak = output_text_sizes[text_size]
                if args.tts:
                    r4a_logger.debug(f"Benchmarking tts for {tts_engine}")
                    if is_supported_voice(lang):
                        r4a_logger.debug(f"Speaking as {tts_engine} text is: {text_to_speak}")
                        speak_response(tts_speaker, text_to_speak, lang=lang)
                    else:
                        r4a_logger.debug(f"Unsupported language {lang} for speaker {tts_engine}")
                #start timing for translation
                r4a_logger.debug(f"Beginning text translation from {lang} to {args.target_lang}")
                translated_text = translate_text(text_to_speak, lang, args.target_lang)
                # end timing for translation
                r4a_logger.debug(f"Translated text from {lang} to {args.target_lang}, result: {translated_text}")
    # benchmark transcribe
    if 'audio_file_dir' in vars(args):
        if is_directory_not_empty(args.audio_file_dir):
            process_audio_files(args.audio_file_dir)

def translate_text(from_text, src_lang, target_lang, device="cpu"):
    src_supported = is_supported_lang(src_lang)
    target_supported = is_supported_lang(target_lang)
    translated_text = None

    trn_latency_csv = 'csv/trn_latency.csv'
    columns = ['Inference Latency', 'Model', 'Translation']
    file_exists = os.path.isfile(trn_latency_csv)
    start = time.time()

    if src_lang != target_lang:
        if src_supported and target_supported:
            # TODO: This section could use a refactor
            match args.translator:
                case 'Google': # calls API -- requires network
                    translated_text = GoogleTranslator(source=src_lang, target=target_lang).translate(from_text)
                case 'Facebook': # local -- edge only
                    tr_model_name = args.translation_model
                    match tr_model_name:
                        case 'facebook/m2m100_418M':
                            tr_model = M2M100ForConditionalGeneration.from_pretrained(tr_model_name)
                            tokenizer = M2M100Tokenizer.from_pretrained(tr_model_name)
                            tokenizer.src_lang = src_lang
                            encoded_lang = tokenizer(from_text, return_tensors="pt")
                            generated_tokens = tr_model.generate(**encoded_lang, forced_bos_token_id=tokenizer.get_lang_id(target_lang))
                            translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
                        case _ if re.match(r'facebook/(hf-)?seamless-m4t-*', tr_model_name):
                            tr_model = SeamlessM4TModel.from_pretrained(tr_model_name)
                            processor = AutoProcessor.from_pretrained(tr_model_name)
                            # Processing the text input
                            # encode for the alpha3 lang
                            src_alpha3_lang_code = Language.get(src_lang).to_alpha3()
                            tgt_alpha3_lang_code = Language.get(target_lang).to_alpha3()
                            r4a_logger.debug(f"Converted lang code '{src_lang}' to alpha3 lang code '{src_alpha3_lang_code}'")
                            # translate src to tgt langauge
                            r4a_logger.debug(f"Translating text from {src_alpha3_lang_code} to {tgt_alpha3_lang_code}")
                            text_inputs = processor(text=from_text, src_lang=src_alpha3_lang_code, return_tensors="pt")
                            output_tokens = tr_model.generate(**text_inputs, tgt_lang=tgt_alpha3_lang_code, 
                                            generate_speech=False)
                            translated_text = processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)
                        case _:
                            r4a_logger.error(f"Unsupported model {tr_model_name} provided. Supported models are: {supported_tr_models}")
                            write_gui_message("assistant", error_emojis)
                case _:
                    r4a_logger.error(f"Unsupported translator provided. Supported translators are: {SUPPORTED_TRANSLATORS}")
                    write_gui_message("assistant", error_emojis) 
        else:
            r4a_logger.error(f"Unsupported language. Requesting translation from {src_lang} (supported:{src_supported}) to {target_lang} (supported:{target_supported})")
            write_gui_message("assistant", error_emojis)
    else:
        r4a_logger.debug(f"Source language '{src_lang}' and target language '{target_lang}' are the same, returning.")
        translated_text = from_text
    end = time.time()
    trn_latency = end - start
    with open(trn_latency_csv, 'a+', newline='') as latency_file:
        writer = csv.writer(latency_file)
        if not file_exists:
            writer.writerow(columns)
        writer.writerow([trn_latency, args.translation_model, translated_text])
    r4a_logger.debug(f"Translated text is: {translated_text}")
    return translated_text

def concat(chunks, collar=0.05):
    """
    Concatenate predictions and audio
    given a list of `(diarization, waveform)` pairs
    and merge contiguous single-speaker regions
    with pauses shorter than `collar` seconds.
    """
    first_annotation = chunks[0][0]
    first_waveform = chunks[0][1]
    annotation = Annotation(uri=first_annotation.uri)
    data = []
    for ann, wav in chunks:
        annotation.update(ann)
        data.append(wav.data)
    annotation = annotation.support(collar)
    window = SlidingWindow(
        first_waveform.sliding_window.duration,
        first_waveform.sliding_window.step,
        first_waveform.sliding_window.start,
    )
    data = np.concatenate(data, axis=0)
    return annotation, SlidingWindowFeature(data, window)

def create_speaker(tts_engine=args.tts_engine):
    global speaker
    if not speaker or args.benchmark_only:
        r4a_logger.debug(f"Creating new speaker of type {tts_engine}")
        match tts_engine:
            case 'espeakng':
                speaker = EspeakngSpeaker(wpm=args.wpm, logger=r4a_logger)
            case 'seamless':
                speaker = SeamlessSpeaker(logger=r4a_logger)
            case 'bark':
                speaker = BarkSpeaker(logger=r4a_logger)
            case 'coqui':
                speaker = CoquiSpeaker(logger=r4a_logger)
    if args.benchmark_only:
        return speaker

def speak_response(speaker, output, lang):
    start = time.time()
    started_at = datetime.datetime.now()
    generated_speech = speaker.generate(output)
    end = time.time()
    ended_at = datetime.datetime.now()
    generation_latency = end - start
    speaker.say(generated_speech, wait4prev=True)
    tts_latency_csv = 'csv/tts_latency.csv'
    columns = ['Inference Latency', 'Source Language', 'Target Language', 'Text Size', 'Started at', 'Ended at']
    file_exists = os.path.isfile(tts_latency_csv)
    with open(tts_latency_csv, 'a+', newline='') as latency_file:
        writer = csv.writer(latency_file)
        if not file_exists:
            writer.writerow(columns)
        writer.writerow([generation_latency, args.source_lang, lang, len(output), started_at, ended_at])
    
def speak_gpt_response(speaker, output, lang=args.target_lang):
    # Mute the microphone so that we don't accidentally respond to the response
    r4a_utils.mute_audio_input_devices(logger=r4a_logger)
    speak_response(speaker, output,lang)
    r4a_utils.mute_audio_input_devices(mute=False, logger=r4a_logger) #unmute

def write_gui_message(role, text):
    r4a_logger.debug(f"Publishing message: {text} as role: {role} to Redis")
    message_data = json.dumps({"text": text, "role": role})
    redis_client.publish('r4a_messages', message_data)

def respond_and_print(colorized_transcriptions_list):
    """
    Print the colorized text from the speaker diarization
    Extract text and send as prompt to ChatGPT
    Input is list of the format {"spk_id": int, "text": str, "lang": str, "color":str}
    """
    r4a_logger.debug(f"colorized_transcriptions_list: {colorized_transcriptions_list}")
    target_lang = args.target_lang
    # strip out data between tags:
    colored_text = []
    all_text = {}
    for transcription in colorized_transcriptions_list:
        text = transcription["text"]
        color = transcription["color"]
        lang = transcription["lang"]
        if color is None:
            color = ""
        r4a_logger.debug(f"color is: {color}")
        colored_text.append(f"[{color}]{text}")
        if args.gui:
            add_translation = f"({lang})->({target_lang})"
            write_gui_message("user", f"{add_translation} {text}")

        if lang in all_text.keys():
            all_text[transcription["lang"]] += f"\n{text}"
        else:
            all_text[lang] = text
    rich.print("\n".join(colored_text)) 

    if args.gpt:
        # append(f"[{colors[speaker]}]{text}")
        if len(all_text.keys()) > 1:
            r4a_logger.debug(f"There are multiple languages spoken: {all_text.keys()}")
        # respond in each language spoken?
        for lang in all_text.keys():
            prompt = all_text[lang]
            r4a_logger.debug(f"Prompt is: {prompt}")
            output = gpt_model.generate(prompt) 
            if lang != target_lang:
                r4a_logger.debug(f"Translating output from {target_lang} to {lang}")
                r4a_logger.debug(f"Original response is {output}")
                output = translate_text(output, target_lang, lang) 
            # To run with GPU, add additional arg: , device='gpu') # device='amd', device='intel'
            # GPT should respond back in the speaker's native language
            print(f"GPT RESPONSE ({target_lang}-->{lang}): {output}")
        if args.gui:
            r4a_logger.debug(f"Response type is {type(output)}")
            if isinstance(output, list):
                for resp in output:
                    write_gui_message("assistant", resp)
            else:
                write_gui_message("assistant", output)
        if args.tts:
            # ensure creation of speaker only happens once
            create_speaker(args.tts_engine)
            if is_supported_voice(lang):
                logging.debug(f"Setting speaker voice to {lang}")
                speaker.voice = lang
                speak_gpt_response(speaker, output, lang=lang)
            else:
                no_read_msg = f"Unable to read response, speaker language {lang} is not supported for TTS"
                translated_no_read = translate_text(no_read_msg, 'en', lang) 
                r4a_logger.warn(f"Unable to read response, speaker language {lang} is not supported for TTS")
                write_gui_message("assistant", translated_no_read)


def colorize_transcription(transcriptions):
    """
    Unify a speaker-aware transcription represented as
    a dict of {spk_id: int, text: str, lang: str} 
    into a single text colored by speakers.
    """
    colors = 2 * [
        "bright_red", "bright_blue", "bright_green", "orange3", "deep_pink1",
        "yellow2", "magenta", "cyan", "bright_magenta", "dodger_blue2"
    ]
    result = []
    r4a_logger.debug(f"In colorize_transcription, transcription is: {transcriptions}")
    for transcription in transcriptions:
        if transcription["spk_id"] == -1:
            # No speakerfound for this text, use default terminal color
            transcription["color"] = None
            result.append(transcription)
        else:
            transcription["color"] = colors[transcription["spk_id"]]
            result.append(transcription)
    r4a_logger.debug(f"Result is: {result}")
    return result

def is_supported_lang(lang, translator=args.translator):
    supported = False
    # https://huggingface.co/facebook/m2m100_418M - Facebook Model
    if translator in SUPPORTED_TRANSLATORS:
        if translator == "Google":
            supported = lang in GoogleTranslator().get_supported_languages(as_dict=True)
        elif translator == "Facebook":
            tr_model_name = args.translation_model
            match tr_model_name:
                case "facebook/m2m100_418M": 
                    tokenizer = M2M100Tokenizer.from_pretrained(tr_model_name)
                    language_codes = list(tokenizer.lang_code_to_id.keys())
                    supported = lang in language_codes
                case _ if re.match(r"facebook/(hf-)?seamless-m4t-*", tr_model_name):
                    # https://github.com/facebookresearch/seamless_communication/blob/main/docs/m4t/README.md#supported-languages
                    # https://raw.githubusercontent.com/facebookresearch/seamless_communication/main/demo/m4tv2/lang_list.py
                    # Would prefer to do a programmatic way such as with m2m100, but couldn't find the supported languages
                    # In the tokenizer or model
                    alpha3_lang_code = Language.get(lang).to_alpha3()
                    r4a_logger.debug(f"Converted 2 char lang code '{lang}' to alpha3 lang code '{alpha3_lang_code}'")
                    supported = alpha3_lang_code in lang_list.text_source_language_codes
                case _:
                    r4a_logger.error(f"Unsupported Facebook model: '{tr_model_name}'")
                    write_gui_message("assistant", error_emojis)

        else:
            supported = False
    else:
        write_gui_message("assistant", error_emojis)
        r4a_logger.error(f"Unsupported translator: {translator}")
    return supported

def is_supported_voice(lang):
        supported_voice = False
        if not speaker:
            r4a_logger.error("No speaker instantiated!")
        supported_voice = speaker.supported_lang(lang)
        return supported_voice

class WhisperTranscriber:
    def __init__(self, model=args.stt_model, device="cpu", whisper_type=args.whisper_type):
        if whisper_type == 'faster':
            self.model = WhisperModel(model, device=device, compute_type="int8")
            self.whisper_type = 'faster'
        else:
            self.model = whisper.load_model(model, device=device)
            self.whisper_type = 'timestamped'
        self._buffer = ""

    def translate_faster(self, audio, start, source_lang=args.source_lang, target_lang=args.target_lang):
        """Detect language and translate audio to desired language"""
        # https://xcelore.com/breaking-language-barriers-with-artificial-intelligence-a-guide-to-audio-translation-using-whisper-and-bark/
        # https://github.com/openai/whisper/blob/main/whisper/tokenizer.py <-- supported languages
        # make log-Mel spectogram and move to same device as the model
        # TODO: device should be intel GPU if available
        if target_lang == source_lang:
            segments, info = self.model.transcribe(self, audio=audio, word_timestamps=True, intial_prompt=args.whisper_prompt, vad_filter=True)
            translation = restruct_transcript(segments, info)
            end_time = time.time()
            r4a_logger.debug(f"Time to generate faster translation (translate func): {end_time - start} seconds")
        else:
            if target_lang == 'en':
                #*When I hit this case, list(segments)[0] is out of range*
                segments, info = self.model.transcribe(audio=audio, language=source_lang, 
                initial_prompt=args.whisper_prompt, task="translate", word_timestamps=True, beam_size=5)
                translation = restruct_transcript(segments, info)
                end_time = time.time()
                r4a_logger.debug(f"Time to generate translation: {end_time - start} seconds")
            else:
                # since whisper only supports translation from lang->english, if the target langauge is not english
                # Use another translator
                # verify that it is a supported language
                # TODO: Change to Facebook model / huggingface transformer to run local w/out cloud
                r4a_logger.debug("Using alternative translation model (target lang != english)")
                if is_supported_lang(target_lang):
                    segments, info = self.model.transcribe(audio=audio, language=source_lang, 
                    initial_prompt=args.whisper_prompt, task="transcribe", word_timestamps=True, beam_size=5)
                    transcription = restruct_transcript(segments, info)
                    end_time = time.time()
                    r4a_logger.debug(f"Time to generate translation: {end_time - start} seconds")
                    text =  transcription['text']
                    segments = transcription['segments']
                    text = translate_text(text, source_lang, target_lang)[0]
                    translation = {
                        "text": text,
                        "language": target_lang,
                        "segments": segments
                    }
                else:
                    raise Exception("Target Language not supported for translation", target_lang)
                    r4a_logger.error(f"Target Language not supported for translation: {target_lang}")

        translation['source_lang'] = source_lang
        return translation

    def transcribe_faster(self, waveform, start):
        """Transcribe audio using Whisper"""
        # Pad/trim audio to fit 30 seconds as required by Whispers
        audio = waveform.data.astype("float32").reshape(-1)
        audio = faster_whisper.audio.pad_or_trim(audio, len(audio))
        # Transcribe the given audio while suppressing logs
        try:
            with r4a_utils.suppress_stdout():
                segments, info = self.model.transcribe(audio, word_timestamps=True, beam_size=5, vad_filter=True)
                transcription = restruct_transcript(segments, info)
                end_time = time.time()
                r4a_logger.debug(f"Time to generate faster translation (transcribe func): {end_time - start} seconds")
                # switch to using the detected langauge from whisper instead of call to cloud method
                source_lang = transcription['language']
                lang_prob = transcription['language_probs'][source_lang]
                r4a_logger.debug(f"Detected language {source_lang} with probability {lang_prob} other potential languages: {transcription['language_probs']}")
                source_lang = single_detection(transcription['text'], args.detection_key)
                target_lang = args.target_lang
                if source_lang != target_lang:
                    r4a_logger.debug(f"The detected langauge {source_lang} is different from the target language {target_lang}")
                    transcription = self.translate_faster(audio, start, source_lang, target_lang)
            transcription['source_lang'] = source_lang
            return transcription
        except AssertionError as e:
            # AssertionError: Inconsistent number of segments: whisper_segments (1) != timestamped_word_segments (0)
            # exit the program
            r4a_logger.error("There was a problem with the AI audio processing, exiting the program!")
            os.kill(os.getpid(), signal.SIGINT)

    def translate_tstamp(self, audio, start, source_lang=args.source_lang, target_lang=args.target_lang, transcript=None):
        """Detect language and translate audio to desired language"""
        # https://xcelore.com/breaking-language-barriers-with-artificial-intelligence-a-guide-to-audio-translation-using-whisper-and-bark/
        # https://github.com/openai/whisper/blob/main/whisper/tokenizer.py <-- supported languages
        # make log-Mel spectogram and move to same device as the model
        # TODO: device should be intel GPU if available

        r4a_logger.debug("In tstamp translate function")
        if target_lang == source_lang:
            r4a_logger.debug("IN ELSE OF ELSE 0.1")
            translation = whisper.transcribe(
                    self.model,
                    audio,
                    # We use past transcriptions to condition the model
                    intial_prompt=args.whisper_prompt,
                    verbose=True  # to avoid progress bar
                )
        else:
            if target_lang == 'en':
                translation = whisper.transcribe(
                    self.model,
                    audio,
                    # We use past transcriptions to condition the model
                    initial_prompt=args.whisper_prompt,
                    language=source_lang,
                    task="translate",
                    verbose=True  # to avoid progress bar
                )
            else:
                # since whisper only supports translation from lang->english, if the target langauge is not english
                # Use another translator
                # verify that it is a supported language
                # TODO: Change to Facebook model / huggingface transformer to run local w/out cloud
                # r4a_logger.debug("In ELSE OF ELSE")
                if is_supported_lang(target_lang):
                    if transcript:
                        transcription = transcript
                    else:
                        transcription = whisper.transcribe(
                            self.model,
                            audio,
                            # We use past transcriptions to condition the model
                            intial_prompt=args.whisper_prompt,
                            verbose=True  # to avoid progress bar
                        )
                    text = translate_text(transcription['text'], source_lang, target_lang)
                    r4a_logger.debug(f"TRANSCRIPT: {transcription}")
                    translation = {
                        "text": text,
                        "language": target_lang,
                        "segments": transcription['segments']
                    }
                else:
                    raise Exception("Target Language not supported for translation", target_lang)
                    r4a_logger.error(f"Target Language not supported for translation: {target_lang}")
        translation['source_lang'] = source_lang
        end_time = time.time()
        r4a_logger.debug(f"Time to generate timestamped translation (translate func): {end_time - start} seconds")
        return translation

    def transcribe_tstamp(self, waveform, start):
        """Transcribe audio using Whisper"""
        # Pad/trim audio to fit 30 seconds as required by Whisper
        audio = waveform.data.astype("float32").reshape(-1)
        audio = whisper.pad_or_trim(audio)

        # Transcribe the given audio while suppressing logs
        try:
            with r4a_utils.suppress_stdout():
                transcription = whisper.transcribe(
                    self.model,
                    audio,
                    # We use past transcriptions to condition the model
                    initial_prompt=args.whisper_prompt,
                    verbose=True  # to avoid progress bar
                )
                # switch to using the detected langauge from whisper instead of call to cloud methond
                source_lang = transcription['language']
                lang_prob = transcription['language_probs'][source_lang]
                r4a_logger.debug(f"Detected language {source_lang} with probability {lang_prob} other potential languages: {transcription['language_probs']}")
                # source_lang = single_detection(transcription['text'], args.detection_key)
                target_lang = args.target_lang
                if source_lang != target_lang:
                    r4a_logger.debug(f"The detected langauge {source_lang} is different from the target language {target_lang}")
                    transcription = self.translate_tstamp(audio, start, source_lang, target_lang, transcript=transcription)
            transcription['source_lang'] = source_lang
            end_time = time.time()
            r4a_logger.debug(f"Time to generate timestamped translation (transcribe func): {end_time - start} seconds")
            return transcription    
        except AssertionError as e:
            # AssertionError: Inconsistent number of segments: whisper_segments (1) != timestamped_word_segments (0)
            # exit the program
            r4a_logger.error("There was a problem with the AI audio processing, exiting the program!")
            write_gui_message("assistant", error_emojis)
            os.kill(os.getpid(), signal.SIGINT)

    def identify_speakers(self, transcription, diarization, time_shift):
        """Iterate over transcription segments to assign speakers"""
        speaker_captions = []
        source_lang = transcription['source_lang']
        speaker_count = 0
        start_time = time.time()
        started_at = datetime.datetime.now()
        for segment in transcription["segments"]:

            # Crop diarization to the segment timestamps
            start = time_shift + segment["words"][0]["start"]
            end = time_shift + segment["words"][-1]["end"]
            dia = diarization.crop(Segment(start, end))

            # Assign a speaker to the segment based on diarization
            speakers = dia.labels()
            num_speakers = len(speakers) 
            speaker_count = num_speakers
            if num_speakers == 0:
                # No speakers were detected
                caption = {"spk_id":-1, "text": segment["text"], "lang": source_lang}
            elif num_speakers == 1:
                # Only one speaker is active in this segment
                spk_id = int(speakers[0].split("speaker")[1])
                caption = {"spk_id": spk_id, "text": segment["text"], "lang": source_lang}
            else:
                # Multiple speakers, select the one that speaks the most
                max_speaker = int(np.argmax([
                    dia.label_duration(spk) for spk in speakers
                ]))
                caption = {"spk_id": max_speaker, "text": segment["text"], "lang": source_lang}
            speaker_captions.append(caption)
        end_time = time.time()
        ended_at = datetime.datetime.now()
        speaker_latency = end_time - start_time
        speaker_latency_csv = 'csv/speaker_latency.csv'
        columns = ['Inference Latency', 'Source Language', 'Speaker Count', 'Started at', 'Ended at']
        file_exists = os.path.isfile(speaker_latency_csv)
        with open(speaker_latency_csv, 'a+', newline='') as latency_file:
            writer = csv.writer(latency_file)
            if not file_exists:
                writer.writerow(columns)
            writer.writerow([speaker_latency, source_lang, speaker_count, started_at, ended_at])

        return speaker_captions

    def __call__(self, diarization, waveform):
        # Step 1: Transcribe
        asr_latency_csv = 'csv/asr_latency.csv'
        columns = ['Inference Latency', 'Whisper Type', 'Transcription Length', 'Started at', 'Ended at']
        file_exists = os.path.isfile(asr_latency_csv)
        start_time = time.time()
        if self.whisper_type == 'faster':
            start = time.time()
            started_at = datetime.datetime.now()
            transcription = self.transcribe_faster(waveform, start_time)
            end = time.time()
            ended_at = datetime.datetime.now()
            asr_latency = end - start
            r4a_logger.debug(f"Transcription: {transcription['segments'][0]['text']}")
            with open(asr_latency_csv, 'a+', newline='') as latency_file:
                writer = csv.writer(latency_file)
                text_len = len(transcription['segments'][0]['text'].split())
                if not file_exists:
                    writer.writerow(columns)
                writer.writerow([asr_latency, self.whisper_type, text_len, started_at, ended_at])
        else:
            file_exists = os.path.isfile(asr_latency_csv)
            start = time.time()
            started_at = datetime.datetime.now()
            transcription = self.transcribe_tstamp(waveform, start_time)
            end = time.time()
            ended_at = datetime.datetime.now()
            asr_latency = end - start
            r4a_logger.debug(f"Transcription: {transcription['segments'][0]['text']}")
            with open(asr_latency_csv, 'a+', newline='') as latency_file:
                writer = csv.writer(latency_file)
                if not file_exists:
                    writer.writerow(columns)
                writer.writerow([asr_latency, self.whisper_type, transcription['segments'][0]['text'], started_at, ended_at])

        # Update transcription buffer
        self._buffer += transcription["text"]
        # The audio may not be the beginning of the conversation
        time_shift = waveform.sliding_window.start
        # Step 2: Assign speakers
        # speaker_transcriptions = self.identify_speakers(segments, info, diarization, time_shift)
        speaker_transcriptions = self.identify_speakers(transcription, diarization, time_shift)
        return speaker_transcriptions

def restruct_transcript(segments, info):
    # Look into why info changes when speaking english/french (includes lang_probs) vs german (doesn't include lang_probs)
    segments = list(segments)
    text = ""
    for segment in segments:
        try:
            seg_no_speech_prob = segment.no_speech_prob
            r4a_logger.debug(f"No speech prob: {seg_no_speech_prob}, (Should be below 0.4)")
            compression_ratio = segment.compression_ratio
            r4a_logger.debug(f"Compression ratio: {compression_ratio}, (Should be below 2)")
            if seg_no_speech_prob < 0.4 and compression_ratio < 2.0:
                text += segment.text + " "
        except Exception:
            pass
    r4a_logger.debug(f"SEGMENTS in restruct: {segments}")
    segments_dict = {}
    segments_dict['text'] = ""
    if segments:
        segments_dict = (segments)[0]._asdict()
    transcription = {}
    info = info._asdict()
    transcription['text'] = segments_dict['text']
    transcription['segments'] = [segments_dict]
    source_lang = info['language']
    transcription['language'] = source_lang
    all_lang_probs = info['all_language_probs']
    r4a_logger.debug(f"reconstruct_transcript (503): all_lang_probs: {all_lang_probs}")
    lang_probs_dict = {}
    if all_lang_probs:
        for lang in all_lang_probs:
            lang_probs_dict[lang[0]] = lang[1]
    transcription['language_probs'] = lang_probs_dict
    transcription['source_lang'] = source_lang
    dict_words = []
    words = transcription['segments'][0]['words']
    for word in words:
        dict_word = {}
        dict_word['text'] = word.word
        dict_word['start'] = word.start
        dict_word['end'] = word.end
        dict_word['confidence'] = word.probability
        dict_words.append(dict_word)
    transcription['segments'][0]['words'] = dict_words
    
    return transcription

def get_microphone_source():
    openai.api_key = args.openapi_key
    # Log in to Hugging Face
    login(token=args.hugging_face_key)

    # If you have a GPU, you can also set device=torch.device("cuda")
    config = SpeakerDiarizationConfig(
        duration=5,
        step=0.5,
        latency="min",
        tau_active=0.5,
        rho_update=0.1,
        delta_new=0.57
    )
    r4a_logger.debug(f"SpeakerDiarazation config: {config}")
    r4a_logger.debug("Getting Speaker Diarization for config")
    dia = SpeakerDiarization(config)
    r4a_logger.debug(f"Completed SpeakerDiarization set up: {dia}")
    r4a_logger.debug(f"in get_microphone_source(): sound_device is: {sound_device}")
    source = MicrophoneAudioSource(device=sound_device['index'])
    r4a_logger.debug(f"Mic source is: {source}")
    global sample_rate 
    sample_rate = 24_000 

    # If you have a GPU, you can also set device="cuda"
    # TODO: Change this to test Intel GPU
    # TODO: Replace model https://github.com/openai/whisper#available-models-and-languages

    r4a_logger.debug("Setting up WhisperTranscriber")
    asr = WhisperTranscriber(model=args.stt_model)
    r4a_logger.debug("Completed transcriber set up")

    # Split the stream into duration s chunks for transcription
    transcription_duration = config.duration 
    # Apply models in batches for better efficiency
    batch_size = int(transcription_duration // config.step)

    # Chain of operations to apply on the stream of microphone audio
    mic_stream_pipe = source.stream.pipe(
        # Format audio stream to sliding windows of 5s with a step of 500ms
        dops.rearrange_audio_stream(
            config.duration, config.step, source.sample_rate
        ),
        ops.map(blocks.Resample(source.sample_rate, config.sample_rate, config.device)),
        # Wait until a batch is full
        # The output is a list of audio chunks
        ops.buffer_with_count(count=batch_size),
        # Obtain diarization prediction
        # The output is a list of pairs `(diarization, audio chunk)`
        ops.map(dia),
        # Concatenate 500ms predictions/chunks to form a single 2s chunk
        ops.map(concat),
        # Ignore this chunk if it does not contain speech
        ops.filter(lambda ann_wav: ann_wav[0].get_timeline().duration() > 0),
        # Obtain speaker-aware transcriptions
        # The output is a list of pairs `(speaker: int, caption: str)`
        ops.starmap(asr),
        # Color transcriptions according to the speaker
        # The output is plain text with color references for rich
        ops.map(colorize_transcription),
    ).subscribe(
        on_next=respond_and_print,  # print colored text and GPT response if using GPT for prompt
        on_error=lambda e: (traceback.print_exception(type(e), e, e.__traceback__)
            if not isinstance(e,SystemExit)
            else r4a_logger.debug("Program exit issued within get_microphone_source, ending captioning and translation")
            ),  # print stacktrace if error is not an issued sys exit by ctrl+c
        on_completed=print("Microphone stream completed"),
        scheduler=scheduler
    )
    r4a_logger.debug(f"Source sample rate: {source.sample_rate} \t Config Sample Rate: {config.sample_rate}")
    return [mic_stream_pipe, source]


def main():
    r4a_logger.debug("Starting application in main")
    if args.benchmark_only:
        r4a_logger.debug("Bencharking speech generation and translation...")
        benchmark_tts_trn()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    r4a_logger.debug("Getting microphone source")
    disposable,mic_stream_pipe = get_microphone_source()
    r4a_logger.debug(f"Mic is: {mic_stream_pipe}")
    handle_audio_stream(mic_stream_pipe, disposable)
    r4a_logger.info("Ending translation and captioning")

if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        print("Caught sys exit")
        pass
    except Exception as e:
        print(f"Unexpected exception occurred: {e}")
        r4a_logger.error(f"Unexpected exception occurred: {e}")
        sys.exit(1)


