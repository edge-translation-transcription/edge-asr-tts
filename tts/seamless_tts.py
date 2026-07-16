import os
import sounddevice as sd
import numpy as np
from huggingface_hub import login
from transformers import SeamlessM4TModel, AutoProcessor
from langcodes import Language
import lang_list # https://raw.githubusercontent.com/facebookresearch/seamless_communication/main/demo/m4tv2/lang_list.py
from baseclass_tts import BaseSpeaker

class SeamlessSpeaker(BaseSpeaker):
    _default_model_name = "facebook/hf-seamless-m4t-medium"
    _default_voice = "eng"
    supported_langs = lang_list.s2st_target_language_codes

    def __init__(self, model_name=None, voice = None, device="cpu",
                 hf_key=None, logger=None):
        if hf_key is not None:
            self.hf_key = hf_key
        else:
            self.hf_key = os.getenv('HF_KEY')
            if self.hf_key is None:
                raise Exception("You must provide a huggingface key to login for using the seamless models!")
                self.logger.error("You must provide a huggingface key to login for using the seamless models!")
        if voice is None:
            voice = SeamlessSpeaker._default_voice
        self.voice = Language.get(voice).to_alpha3()
        self.logger = logger
        self.model_name = model_name
        if self.model_name is None:
            print(f"using default model name {SeamlessSpeaker._default_model_name}")
            self.model_name = SeamlessSpeaker._default_model_name
        self.processor = AutoProcessor.from_pretrained(self.model_name)
        self.model = SeamlessM4TModel.from_pretrained(self.model_name)

    @classmethod
    def supported_lang(cls, lang):
        alpha3_lang_code = Language.get(lang).to_alpha3()
        supported = alpha3_lang_code in cls.supported_langs
        return supported

    @property
    def hf_key(self):
        return self.__hf_key
    
    @hf_key.setter
    def hf_key(self, value):
        login(token=value)
        self.__hf_key = value

    @property
    def voice(self):
        return self.__voice

    @voice.setter
    def voice(self, value):
        if not SeamlessSpeaker.supported_lang(value):
            raise Exception(f"Attempt to set unsupported voice {value}")
            self.logger.error(f"Attempt to set unsupported voice {value}")
        alpha3_lang_code = Language.get(value).to_alpha3()
        self.__voice = alpha3_lang_code

    def generate(self, output):
        if self.logger is not None:
            self.logger.debug(f"SPEAK RESPONSE USING '{self.model_name}', in lang '{self.voice}' sample rate: {self.model.config.sampling_rate}")
        
        text_inputs = self.processor(text = output, src_lang=self.voice, return_tensors="pt")
        audio_array = self.model.generate(**text_inputs, tgt_lang=self.voice)[0].cpu().numpy().squeeze()
        audio_data = np.array(audio_array)
        return audio_data

    def say(self, input, wait4prev=True):
        # https://huggingface.co/facebook/seamless-m4t-medium/discussions/10 - error prone audio
        # If sample rate is not provided
        # The default sampling rate of this corpus is 48000, whereas the SeamlessM4T model was 
        # trained with audio of 16000 Hz
        sd.play(input, self.model.config.sampling_rate)
        if wait4prev:
            sd.wait()

def main():
    # Instantiate the speaker
    voice = "eng"
    tts_text = "Hello, testing seamless text-to-speech"
    hf_key = os.getenv('HF_KEY')
    if hf_key is None:
        hf_key = input("Provide a huggingface key for login: ")
    speaker = SeamlessSpeaker(voice=voice, hf_key=hf_key)

    # generate the speech
    generated_speech = speaker.generate(tts_text)
    speaker.say(generated_speech)

    # Print the list of the forst 10 languages
    num_supported_langs = len(SeamlessSpeaker.supported_langs)

    print(f"There are {num_supported_langs} supported languages for seamless tts")
    num_langs_printed = 0

    for iso_code in speaker.supported_langs:
        if num_langs_printed > 10:
            break
        print(f"Iso Code: {iso_code}")
        num_langs_printed += 1

if __name__ == "__main__":
    main()

