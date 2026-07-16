import os
from pathlib import Path
import tts.ov_utils as ov_utils
import openvino as ov
import sounddevice as sd
import numpy as np
import torch
from types import SimpleNamespace
from bark.generation import load_model, SUPPORTED_LANGS
from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
from baseclass_tts import BaseSpeaker

class BarkSpeaker(BaseSpeaker):
    _default_sample_rate = SAMPLE_RATE
    _default_voice = "en"
    _default_model_name = f"tts_models/{_default_voice}/fairseq/vits"
    lang_codes = [code for name, code in SUPPORTED_LANGS]
    _default_model_path = "/usr/app/models"

    @classmethod
    def supported_lang(cls, lang):
        return lang in cls.lang_codes

    def __init__(self, model_name=None, voice=None, logger=None,
                 device="cpu", use_openvino= False, model_path=None,
                 use_small=True, force_reload=False):
        
        self.model_name = model_name
        self.voice = voice
        self.logger = logger
        self.device = device
        self.use_openvino = use_openvino
        self.ov_vars = SimpleNamespace()
        if self.device.upper() == "CPU":
            os.environ["SUNO_OFFLOAD_CPU"] = "True"
        if use_small:
            os.environ["SUNO_USE_SMALL_MODELS"] = "True" # Use smaller models to fit into 8GB VRAM
        # Download and load all models
        preload_models()

        if self.use_openvino:
            # TODO: There's a lot of redundancy here, clean this up later

            self.ov_vars.model_types = ["fine", "coarse", "text"]
            self.ov_vars.model_path = model_path
            if model_path is None:
                self.ov_vars.model_path = BarkSpeaker._default_model_path
            self.ov_vars.model_path_dir = Path(os.path.basename(self.ov_vars.model_path))
            self.ov_vars.use_small = use_small
            self.ov_vars.use_gpu = device == "cpu" # set to True or False depending on value of device
            self.ov_vars.force_reload = force_reload

            # Text model setup
            self.ov_vars.text_encoder = None
            self.ov_vars.ov_text_model = None
            self.ov_vars.text_model_suffix = "_small" if self.ov_vars.use_small else ""
            self.ov_vars.text_model_dir = self.ov_vars.model_path_dir / f"text_encoder{self.ov_vars.text_model_suffix}"
            self.ov_vars.text_encoder_path1 = self.ov_vars.text_model_dir / "bark_text_encoder_1.xml"
            self.ov_vars.text_encoder_path0 = self.ov_vars.text_model_dir / "bark_text_encoder_0.xml"
        
            # Coarse model setup
            self.ov_vars.coarse_model = None
            self.ov_vars.ov_coarse_model = None
            self.ov_vars.coarse_model_suffix = "_small" if self.use_small else ""
            self.ov_vars.coarse_model_dir = self.ov_vars.model_path_dir / f"coarse{self.ov_vars.coarse_model_suffix}"
            self.ov_vars.coarse_encoder_path = self.ov_vars.coarse_model_dir / "bark_coarse_encoder.xml"

            # Fine model setup
            self.fine_model = None
            self.ov_fine_model = None
            self.fine_model_suffix = "_small" if self.use_small else ""
            self.fine_model_dir = self.model_path_dir / f"fine_model{self.fine_model_suffix}"
            self.fine_feature_extractor_xml = self.fine_model_dir / "bark_fine_feature_extractor.xml"

            # Do the work of converting and loading the models

            self._make_model_paths()
            for model_type in self.ov_vars.model_types:
                self._load_models(model_type)
            self._convert_and_save_models()
            self._load_ov_models()

    @property
    def voice(self):
        return self.__voice

    @voice.setter
    def voice(self, value):
        if not BarkSpeaker.supported_lang(value):
            raise Exception(f"Attempt to set unsupported voice {value}")
            self.logger.error(f"Attempt to set unsupported voice {value}")
        self.__voice = value

    def _make_model_paths(self):
        if self.logger is not None:
            self.logger.debug("Calling _make_model_paths")
        self.ov_vars.model_path_dir.mkdir(exist_ok=True)
        self.ov_vars.text_model_dir.mkdir(exist_ok=True)
        self.ov_vars.coarse_model_dir.mkdir(exist_ok=True)
        if self.logger is not None:
            self.logger.debug("completed creation of text and coarse model paths")
        self.ov_vars.fine_model_dir.mkdir(exist_ok=True)
        if self.logger is not None:
            self.logger.debug("completed creation of fine model paths")


    def _load_models(self, model_type):
        match model_type:
            case "text":
                self.ov_vars.text_encoder = load_model(model_type=model_type, use_gpu=self.ov_vars.use_gpu,
                                    use_small=self.ov_vars.use_small, force_reload=self.ov_vars.force_reload)
            case "coarse":
                self.ov_vars.coarse_model = load_model(model_type=model_type, use_gpu=self.ov_vars.use_gpu, 
                                    use_small=self.ov_vars.use_small, force_reload=self.ov_vars.force_reload)
            case "fine":
                self.ov_vars.fine_model = load_model(model_type=model_type, use_gpu=self.ov_vars.use_gpu, 
                                use_small=self.ov_vars.use_small, force_reload=self.force_reload)
            case _:
                if self.logger is not None:
                    self.logger.warn(f"No model of type {model_type}")

    def _convert_and_save_models(self):
        ov_utils.text_encoder_save_and_convert(self.ov_vars.text_encoder_path0, self.ov_vars.text_encoder_path1, 
                                               self.ov_vars.text_encoder)
        ov_utils.coarse_encoder_save_and_convert(self.ov_vars.coarse_encoder_path, self.ov_vars.coarse_model)
        ov_utils.fine_extractor_save_and_convert(self.ov_vars.fine_feature_extractor_xml, self.ov_vars.fine_model_dir,
                                                  self.ov_vars.fine_model)

    def _load_ov_models(self):
        if self.logger is not None:
            self.logger.debug('loading ov_bark model... ')
        core = ov.Core()
        self.ov_vars.ov_text_model = ov_utils.OVBarkTextEncoder(core, self.device, self.ov_vars.text_encoder_path0, 
                                                        self.ov_vars.text_encoder_path1)
        self.ov_vars.ov_coarse_model = ov_utils.OVBarkEncoder(core, self.device, self.ov_vars.coarse_encoder_path)
        self.ov_vars.ov_fine_model = ov_utils.OVBarkFineEncoder(core, self.device, self.ov_vars.fine_model_dir)
        if self.logger is not None:
            self.logger.debug(f"OV TEXT MODEL: {self.ov_vars.ov_text_model}")
            self.logger.debug('loaded ov_bark model... ')

    def generate(self, output, sample_rate=SAMPLE_RATE):
        if self.logger is not None:
            self.logger.debug(f"SPEAK RESPONSE USING BARK, sample rate: {sample_rate}")
        torch.manual_seed(42)
        if self.logger is not None:
            self.logger.debug(f"TEXT TO ORATE: {output}")
            if self.use_openvino:
                self.logger.debug(f"OV TEXT MODEL: {self.ov_text_model}")
        audio_array = generate_audio(output) # shouldn't need to specify voice, accent/langauge should be autodetected from text
        audio_data = np.array(audio_array)
        return audio_data

    def say(self, input, wait4prev=True, sample_rate=SAMPLE_RATE):
        sd.play(input, sample_rate)
        if wait4prev:
            sd.wait()

def main():
    # Instantiate the speaker
    voice = "en"
    model_name = "bark"
    tts_text = "Hello, testing bark text-to-speech"
    
    speaker = BarkSpeaker(model_name, voice)

    # generate the speech
    generated_speech = speaker.generate(tts_text)
    speaker.say(generated_speech)

    # Print the list of the forst 10 languages
    num_supported_langs = len(BarkSpeaker.lang_codes)

    print(f"There are {num_supported_langs} supported languages for bark tts")
    num_langs_printed = 0

    for language_name, iso_code in SUPPORTED_LANGS:
        if num_langs_printed > 10:
            break
        print(f"Iso Code: {iso_code}, Language Name: {language_name}")
        num_langs_printed += 1

if __name__ == "__main__":
    main()
