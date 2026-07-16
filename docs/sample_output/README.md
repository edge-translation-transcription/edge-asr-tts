# Sample Output

GUI 

![Screenshot from 2024-04-26 15-57-19](https://github.com/eshenayo/r4a/assets/8902109/d3447928-daee-4023-aec8-160b9aab04b4)


```console
openvino@dda192ffde22:/usr/app/src$ python3 ./diart_whisper.py --help

usage: diart_whisper.py [-h] [--source_lang SOURCE_LANG] [--target_lang TARGET_LANG] [--openapi_key OPENAPI_KEY] [--detection_key DETECTION_KEY] [--hugging_face_key HUGGING_FACE_KEY]
                        [--tts_model TTS_MODEL] [--stt_model STT_MODEL] [--translation_model TRANSLATION_MODEL] [--translator TRANSLATOR] [--log_level LOG_LEVEL] [--gpt] [--nogpt] [--openvino] [--tts]
                        [--preload_models] [--model_path MODEL_PATH] [--gpt4all_model GPT4ALL_MODEL]

This program take microphone input and translates between multiple speakers or privdes a response from a chatbot

options:
  -h, --help            show this help message and exit
  --source_lang SOURCE_LANG
                        The source language being spoken (default: en)
  --target_lang TARGET_LANG
                        The target languge to translate to (default: en)
  --openapi_key OPENAPI_KEY
                        oAuth key for OpenAPI (default: YOUR KEY - REDACTED)
  --detection_key DETECTION_KEY
                        Key to log into language detection website (default: YOUR KEY - REDACTED)
  --hugging_face_key HUGGING_FACE_KEY
                        Hugging face oAuth key (default: YOUR KEY - REDACTED)
  --tts_model TTS_MODEL
                        name of the text to speech model (default: )
  --stt_model STT_MODEL
                        name of the speech to text model (default: small)
  --translation_model TRANSLATION_MODEL
                        Name of the translation model (default: facebook/m2m100_418M)
  --translator TRANSLATOR
                        The translation provider, must be one of [Google, Facebook] (default: Facebook)
  --log_level LOG_LEVEL
                        Log Level (default: DEBUG)
  --gpt                 Respond to input using ChatGPT (default: True)
  --nogpt               Turn off ChatGPT response (default: False)
  --openvino            Use OpenVINO to optimize the model (default: False)
  --tts                 Read response aloud (default: True)
  --preload_models      Download all models up front to the model_path (default: True)
  --model_path MODEL_PATH
                        The path where AI models are stored (default: /usr/app/models)
  --gpt4all_model GPT4ALL_MODEL
                        GPT4All model name (default: orca-mini-3b-gguf2-q4_0.gguf)

```

![image](https://github.com/eshenayo/r4a/assets/8902109/21af6c33-8d14-4ceb-af5f-07e168d06967)

![image](https://github.com/eshenayo/r4a/assets/8902109/17fd1314-aeba-440e-92ef-3c1d41bbbac5)

## Additional Language Output

* [English to English](./README-en-en.md)
* [Spanish to English](./README-es-en.md)
* [Hindi to English](./README-hi-en.md)
* [Portugese to English](./README-pt-en.md)
* [Mandarin to English](./README-zh-en.md)

[Back to main page](../../README.md)
