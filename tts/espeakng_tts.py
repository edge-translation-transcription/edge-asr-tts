import espeakng
import time
from baseclass_tts import BaseSpeaker

class EspeakngSpeaker(BaseSpeaker):
    supported_langs = espeakng.Speaker.list_voices()
    _default_voice = "en"

    def __init__ (self, wpm=140, voice=None, logger=None):
        self.speaker = espeakng.Speaker()
        self.speaker.wpm = wpm
        if voice is None:
            self.voice = EspeakngSpeaker._default_voice
        else:
            self.voice = voice
        self.logger = logger

    @classmethod
    def supported_lang(cls, lang):
        # Parse the languages if not already done
        if cls._parsed_languages is None:
            cls._parse_languages()

    @classmethod
    def supported_lang(cls, lang):
        return lang in cls.supported_langs

    @property
    def voice(self):
        return self.__voice

    @voice.setter
    def voice(self, value):
        if not EspeakngSpeaker.supported_lang(value):
            raise Exception(f"Attempt to set unsupported voice {value}")
            self.logger.error(f"Attempt to set unsupported voice {value}")
        self.__voice = value
        self.speaker.voice = value

    def generate(self, output):
        # Since this mode of speech output is simply synthesis
        # We are not actually doing any generation, just pass through 
        # The supplied text.
        return output

    def say(self, output, wait4prev=True):
        self.speaker.say(output, wait4prev=wait4prev)
        while self.speaker.prevproc.poll() is None:
            time.sleep(0.5)

def main():
    # Instantiate the speaker
    voice = "es"
    model_name = "espeak"
    tts_text = f"Hola, estoy probando la generación de voz de {model_name}"
    
    speaker = EspeakngSpeaker(voice=voice)

    # generate the speech
    generated_speech = speaker.generate(tts_text)
    speaker.say(generated_speech)

    # Print the list of the forst 10 languages
    num_supported_langs = len(EspeakngSpeaker.supported_langs)

    print(f"There are {num_supported_langs} supported languages for {model_name} tts")
    num_langs_printed = 0

    for iso_code in speaker.supported_langs:
        if num_langs_printed > 10:
            break
        print(f"Iso Code: {iso_code}")
        num_langs_printed += 1

if __name__ == "__main__":
    main()

        
