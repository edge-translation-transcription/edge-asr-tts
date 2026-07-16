import torch
import os
import re
import fairseq_html_parser
import r4a_utils
from pathlib import Path
from TTS.api import TTS
from langcodes import Language
from baseclass_tts import BaseSpeaker


class CoquiSpeaker(BaseSpeaker):
    # Class variable to store the parsed languages
    _parsed_languages = None
    _default_voice = "eng"
    _default_model_name = f"tts_models/{_default_voice}/fairseq/vits"
    _lang_filename = "fairseq_support_tts_langs.html"

    def __init__(self, model_name=None, voice=None, logger=None,
                 device="cpu"):
        self.logger = logger
        self.device = device
        if voice is None:
            voice = CoquiSpeaker._default_voice
        self.voice = Language.get(voice).to_alpha3()
        if model_name is None:
            model_name = CoquiSpeaker._default_model_name
        self.model_name = model_name
        self.model = TTS(model_name=self.model_name).to(self.device)
        CoquiSpeaker._parse_languages()
        self.languages = [iso_code for iso_code, language_name in list(CoquiSpeaker._parsed_languages)[1:]]

    @classmethod
    def _parse_languages(cls):
        if cls._parsed_languages is not None:
            return
        current_dir = Path(__file__).parent
        lang_file_path = current_dir / cls._lang_filename
        if os.path.exists(lang_file_path):
            try:
                with open(lang_file_path, 'r', encoding='utf-8') as file:
                    html_data = file.read()
                fairseq_parser = fairseq_html_parser.FairseqHTMLParser()
                fairseq_parser.feed(html_data)
                cls._parsed_languages = fairseq_parser.languages
            except Exception as e:
                #print(f"Error occurred: {e}")
                self.logger.error(f"Error occurred: {e}")
        else:
            print(f"No such file or directory: {lang_file_path}")

    @classmethod
    def supported_lang(cls, lang):
        # Parse the languages if not already done
        if cls._parsed_languages is None:
            cls._parse_languages()

        # Check if the language is supported
        alpha3_lang_code = Language.get(lang).to_alpha3()
        supported = alpha3_lang_code in [iso_code for iso_code, language_name in list(cls._parsed_languages)[1:]]
        return supported

    @property
    def model_name(self):
        return self.__model_name
    
    @model_name.setter
    def model_name(self, value):
        if not self._validate_model_name(value):
            raise ValueError("Invalid model name")
        self.__model_name = value
    
    @property
    def voice(self):
        return self.__voice

    @voice.setter
    def voice(self, value):
        alpha3_lang_code = Language.get(value).to_alpha3()
        if not CoquiSpeaker.supported_lang(alpha3_lang_code):
            raise Exception(f"Attempt to set unsupported voice {value}")
            self.logger.error(f"Attempt to set unsupported voice {value}")
        self.__voice = alpha3_lang_code
        self.model_name = f"tts_models/{self.__voice}/fairseq/vits"
        self.model = TTS(model_name=self.model_name).to(self.device)

    def _validate_model_name(self, model_name):
        # Construct the expected pattern using self.voice
        pattern = rf"^tts_models/{self.voice}/fairseq/vits$"
        # Use regular expression to match the model_name with the pattern
        return re.match(pattern, model_name) is not None

    def generate(self, output):
        if self.logger is not None:
            self.logger.debug(f"SPEAK RESPONSE USING coqui")
        output_file = "/tmp/output.wav"
        self.model.tts_to_file(output, file_path=output_file)
        return output_file

    def say(self, input, wait4prev=True):
        r4a_utils.play_wav(input, wait4prev)


def main():
    # Instantiate the speaker
    voice = "eng"
    model_name = f"tts_models/{voice}/fairseq/vits"
    tts_text = "Hello, testing coqui text-to-speech"
    
    speaker = CoquiSpeaker(model_name, voice)

    # generate the speech
    generated_speech = speaker.generate(tts_text)
    speaker.say(generated_speech)

    # Print the list of the forst 10 languages
    num_supported_langs = len(CoquiSpeaker._parsed_languages)

    print(f"There are {num_supported_langs} supported languages for coqui tts")
    num_langs_printed = 0

    for iso_code, language_name in speaker._parsed_languages:
        if num_langs_printed > 10:
            break
        print(f"Iso Code: {iso_code}, Language Name: {language_name}")
        num_langs_printed += 1

if __name__ == "__main__":
    main()
