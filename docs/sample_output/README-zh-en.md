# MANDARIN - ENGLISH
![image](./screenshots/chinese-english-screenshot.png)

```console
[?2004h]0;openvino@ac1ac0ba9dd5: /usr/app/srcopenvino@ac1ac0ba9dd5:/usr/app/src$ ./retail_for_all.sh 
[?2004l
Redis is already running with PID: 15
Launching GUI
Killing streamlit process with PID: 9926
[0m
[34m[1m  You can now view your Streamlit app in your browser.[0m
[0m
[34m  Network URL: [0m[1mhttp://172.17.0.2:8501[0m
[34m  External URL: [0m[1mhttp://198.175.113.99:8501[0m
[0m
DEBUG:__main__:curr_sound_device = {'index': 0, 'structVersion': 2, 'name': 'HDA Intel PCH: ALC256 Analog (hw:0,0)', 'hostApi': 0, 'maxInputChannels': 2, 'maxOutputChannels': 0, 'defaultLowInputLatency': 0.005804988662131519, 'defaultLowOutputLatency': -1.0, 'defaultHighInputLatency': 0.034829931972789115, 'defaultHighOutputLatency': -1.0, 'defaultSampleRate': 44100.0}
DEBUG:__main__:curr_sound_device = {'index': 1, 'structVersion': 2, 'name': 'HDA Intel PCH: HDMI 0 (hw:0,3)', 'hostApi': 0, 'maxInputChannels': 0, 'maxOutputChannels': 2, 'defaultLowInputLatency': -1.0, 'defaultLowOutputLatency': 0.005804988662131519, 'defaultHighInputLatency': -1.0, 'defaultHighOutputLatency': 0.034829931972789115, 'defaultSampleRate': 44100.0}
DEBUG:__main__:curr_sound_device = {'index': 2, 'structVersion': 2, 'name': 'HDA Intel PCH: HDMI 1 (hw:0,7)', 'hostApi': 0, 'maxInputChannels': 0, 'maxOutputChannels': 6, 'defaultLowInputLatency': -1.0, 'defaultLowOutputLatency': 0.005804988662131519, 'defaultHighInputLatency': -1.0, 'defaultHighOutputLatency': 0.034829931972789115, 'defaultSampleRate': 44100.0}
DEBUG:__main__:curr_sound_device = {'index': 3, 'structVersion': 2, 'name': 'HDA Intel PCH: HDMI 2 (hw:0,8)', 'hostApi': 0, 'maxInputChannels': 0, 'maxOutputChannels': 8, 'defaultLowInputLatency': -1.0, 'defaultLowOutputLatency': 0.005804988662131519, 'defaultHighInputLatency': -1.0, 'defaultHighOutputLatency': 0.034829931972789115, 'defaultSampleRate': 44100.0}
DEBUG:__main__:curr_sound_device = {'index': 4, 'structVersion': 2, 'name': 'HDA Intel PCH: HDMI 3 (hw:0,9)', 'hostApi': 0, 'maxInputChannels': 0, 'maxOutputChannels': 8, 'defaultLowInputLatency': -1.0, 'defaultLowOutputLatency': 0.005804988662131519, 'defaultHighInputLatency': -1.0, 'defaultHighOutputLatency': 0.034829931972789115, 'defaultSampleRate': 44100.0}
DEBUG:__main__:curr_sound_device = {'index': 5, 'structVersion': 2, 'name': 'sysdefault', 'hostApi': 0, 'maxInputChannels': 128, 'maxOutputChannels': 0, 'defaultLowInputLatency': 0.021333333333333333, 'defaultLowOutputLatency': -1.0, 'defaultHighInputLatency': 0.021333333333333333, 'defaultHighOutputLatency': -1.0, 'defaultSampleRate': 48000.0}
DEBUG:__main__:curr_sound_device = {'index': 6, 'structVersion': 2, 'name': 'hdmi', 'hostApi': 0, 'maxInputChannels': 0, 'maxOutputChannels': 2, 'defaultLowInputLatency': -1.0, 'defaultLowOutputLatency': 0.005804988662131519, 'defaultHighInputLatency': -1.0, 'defaultHighOutputLatency': 0.034829931972789115, 'defaultSampleRate': 44100.0}
DEBUG:__main__:curr_sound_device = {'index': 7, 'structVersion': 2, 'name': 'samplerate', 'hostApi': 0, 'maxInputChannels': 128, 'maxOutputChannels': 0, 'defaultLowInputLatency': 0.007755102040816327, 'defaultLowOutputLatency': -1.0, 'defaultHighInputLatency': 0.023219954648526078, 'defaultHighOutputLatency': -1.0, 'defaultSampleRate': 44100.0}
DEBUG:__main__:curr_sound_device = {'index': 8, 'structVersion': 2, 'name': 'speexrate', 'hostApi': 0, 'maxInputChannels': 128, 'maxOutputChannels': 0, 'defaultLowInputLatency': 0.007755102040816327, 'defaultLowOutputLatency': -1.0, 'defaultHighInputLatency': 0.023219954648526078, 'defaultHighOutputLatency': -1.0, 'defaultSampleRate': 44100.0}
DEBUG:__main__:curr_sound_device = {'index': 9, 'structVersion': 2, 'name': 'pulse', 'hostApi': 0, 'maxInputChannels': 32, 'maxOutputChannels': 32, 'defaultLowInputLatency': 0.008684807256235827, 'defaultLowOutputLatency': 0.008684807256235827, 'defaultHighInputLatency': 0.034807256235827665, 'defaultHighOutputLatency': 0.034807256235827665, 'defaultSampleRate': 44100.0}
DEBUG:__main__:Args source_lang = en
DEBUG:__main__:Args target_lang = en
DEBUG:__main__:Args openapi_key = KEY_VALUE_REDACTED
DEBUG:__main__:Args detection_key = KEY_VALUE_REDACTED
DEBUG:__main__:Args hugging_face_key = KEY_VALUE_REDACTED
DEBUG:__main__:Args tts_model = 
DEBUG:__main__:Args stt_model = small
DEBUG:__main__:Args translation_model = facebook/m2m100_418M
DEBUG:__main__:Args translator = Facebook
DEBUG:__main__:Args log_level = DEBUG
DEBUG:__main__:Args gpt = True
DEBUG:__main__:Args nogpt = False
DEBUG:__main__:Args openvino = False
DEBUG:__main__:Args tts = True
DEBUG:__main__:Args wpm = 140
DEBUG:__main__:Args whisper_prompt = The sentence may be cut off, do not make up words to fill in the rest of the sentence
DEBUG:__main__:Args gui = True
DEBUG:__main__:Args preload_models = False
DEBUG:__main__:Args model_path = /usr/app/models
DEBUG:__main__:Args gpt4all_model = orca-mini-3b-gguf2-q4_0.gguf
DEBUG:__main__:Loading GPT model
Token has not been saved to git credential helper. Pass `add_to_git_credential=True` if you want to set the git credential as well.
Token is valid (permission: read).
Your token has been saved to /home/openvino/.cache/huggingface/token
Login successful
Lightning automatically upgraded your loaded checkpoint from v1.5.4 to v2.2.3. To apply the upgrade to your files permanently, run `python -m pytorch_lightning.utilities.upgrade_checkpoint ../../../home/openvino/.cache/torch/pyannote/models--pyannote--segmentation/snapshots/2ffce0501d0aecad81b43a06d538186e292d0070/pytorch_model.bin`
Model was trained with pyannote.audio 0.0.1, yours is 3.0.1. Bad things might happen unless you revert pyannote.audio to 0.x.
Model was trained with torch 1.10.0+cu102, yours is 2.2.2+cu121. Bad things might happen unless you revert torch to 1.x.
Lightning automatically upgraded your loaded checkpoint from v1.2.7 to v2.2.3. To apply the upgrade to your files permanently, run `python -m pytorch_lightning.utilities.upgrade_checkpoint ../../../home/openvino/.cache/torch/pyannote/models--pyannote--embedding/snapshots/c6335d8f1cd77b30084387468a6cf26fea90009b/pytorch_model.bin`
Model was trained with pyannote.audio 0.0.1, yours is 3.0.1. Bad things might happen unless you revert pyannote.audio to 0.x.
Model was trained with torch 1.8.1+cu102, yours is 2.2.2+cu121. Bad things might happen unless you revert torch to 1.x.
Lightning automatically upgraded your loaded checkpoint from v1.2.7 to v2.2.3. To apply the upgrade to your files permanently, run `python -m pytorch_lightning.utilities.upgrade_checkpoint ../../../home/openvino/.cache/torch/pyannote/models--pyannote--embedding/snapshots/c6335d8f1cd77b30084387468a6cf26fea90009b/pytorch_model.bin`
Model was trained with pyannote.audio 0.0.1, yours is 3.0.1. Bad things might happen unless you revert pyannote.audio to 0.x.
Model was trained with torch 1.8.1+cu102, yours is 2.2.2+cu121. Bad things might happen unless you revert torch to 1.x.
Microphone stream completed
DEBUG:__main__:Source sample rate: 16000 	 Config Sample Rate: 16000
INFO:__main__:Starting translation and captioning, begin speaking...
DEBUG:__main__:Detected language zh with probability 0.9001479148864746 other potential languages: {'en': 0.08325161784887314, 'zh': 0.9001479148864746, 'de': 0.0007455875747837126, 'es': 0.0007287231856025755, 'ru': 0.0008300751796923578, 'ko': 0.0035407133400440216, 'fr': 0.00014781250501982868, 'ja': 0.0011203509056940675, 'pt': 0.0011118209222331643, 'tr': 0.00039763946551829576, 'pl': 0.00013413556735031307, 'ca': 1.538027277092624e-06, 'nl': 2.440857315377798e-05, 'ar': 0.00016347299970220774, 'sv': 4.602471017278731e-05, 'it': 5.075025910628028e-05, 'id': 0.00013105382095091045, 'hi': 0.00017699987802188843, 'fi': 6.6467719079810195e-06, 'vi': 0.0027457696851342916, 'he': 1.122912067330617e-06, 'uk': 9.491044693277217e-06, 'el': 2.6872858143178746e-06, 'ms': 0.00024119825684465468, 'cs': 1.7296340956818312e-05, 'ro': 1.9702732970472425e-05, 'da': 4.21469121647533e-06, 'hu': 7.738637941656634e-05, 'ta': 3.2900912628974766e-05, 'no': 1.654241896176245e-05, 'th': 0.0005189783405512571, 'ur': 7.244074367918074e-05, 'hr': 1.0585142717900453e-06, 'bg': 9.304768013862486e-07, 'lt': 2.1631539937061461e-07, 'la': 0.00021127256331965327, 'mi': 1.1096609341620933e-05, 'ml': 4.55013032478746e-05, 'cy': 0.0001549253793200478, 'sk': 1.1197627145520528e-06, 'te': 1.0385730092821177e-05, 'fa': 3.511771865305491e-05, 'lv': 4.42954359414216e-07, 'bn': 9.250898074242286e-06, 'sr': 7.090470717230346e-07, 'az': 6.187273697833007e-07, 'sl': 2.8990198188694194e-06, 'kn': 1.7194388135521876e-07, 'et': 1.0098000302605215e-07, 'mk': 3.2155817564216704e-08, 'br': 1.7244903574464843e-05, 'eu': 2.219053158114548e-06, 'is': 3.0910877057976904e-07, 'hy': 2.539373156196234e-07, 'ne': 2.975811185024213e-06, 'mn': 1.1148905286972877e-05, 'bs': 9.489139074503328e-07, 'kk': 6.218264729795919e-07, 'sq': 2.6518537765696237e-07, 'sw': 2.674132474567159e-06, 'gl': 7.6147130130266305e-06, 'mr': 1.1503916397259673e-07, 'pa': 3.4892514122475404e-07, 'si': 1.6017307643778622e-05, 'km': 0.00014566264871973544, 'sn': 1.4587332771043293e-05, 'yo': 2.0445069822017103e-05, 'so': 2.4886320559858177e-08, 'af': 3.0211964485715725e-07, 'oc': 9.081061875804153e-07, 'ka': 1.7026730247948763e-08, 'be': 1.211266180689563e-06, 'tg': 1.1026437540806455e-09, 'sd': 3.136639179501799e-06, 'gu': 4.0649695165484445e-08, 'am': 6.1758664848809985e-09, 'yi': 2.7585317639022833e-06, 'lo': 4.0829231693351176e-06, 'uz': 3.391199820956814e-11, 'fo': 3.3977021303144284e-06, 'ht': 4.563695711112814e-06, 'ps': 2.3786164149441902e-07, 'tk': 2.8010904706832207e-10, 'nn': 0.0018983078189194202, 'mt': 6.285017661866732e-08, 'sa': 5.319195406627841e-05, 'lb': 2.7726790308157945e-10, 'my': 6.076953650335781e-05, 'bo': 1.833974602050148e-05, 'tl': 7.928843115223572e-05, 'mg': 4.125985664238385e-11, 'as': 7.146245479816571e-07, 'tt': 1.795260745618421e-10, 'haw': 0.0003809672489296645, 'ln': 6.138242980568975e-08, 'ha': 1.5788458040955078e-10, 'ba': 2.701422974205059e-10, 'jw': 0.00024133859551511705, 'su': 5.887859089170888e-10}
DEBUG:__main__:The detected langauge zh is different from the target language en
DEBUG:__main__:In translate function
DEBUG:__main__:In colorize_transcription, transcription is: [{'spk_id': 0, 'text': ' Hello', 'lang': 'zh'}]
DEBUG:__main__:Result is: [{'spk_id': 0, 'text': ' Hello', 'lang': 'zh', 'color': 'bright_red'}]
DEBUG:__main__:colorized_transcriptions_list: [{'spk_id': 0, 'text': ' Hello', 'lang': 'zh', 'color': 'bright_red'}]
DEBUG:__main__:color is: bright_red
DEBUG:__main__:Publishing message: (zh)->(en)  Hello as role: user to Redis
[91m Hello[0m
DEBUG:__main__:Prompt is:  Hello
DEBUG:__main__:Translating output from en to zh
DEBUG:__main__:Original response is , I am interested in purchasing a used car from your dealership. Can you please provide me with some information about the car such as its make and model, year of manufacture, any special features or options, and the price range?
GPT RESPONSE (en-->zh): ['我有兴趣从您的经销商购买一辆使用的汽车,请给我一些关于汽车的信息,如它的制作和模型,生产年份,任何特殊的功能或选项,以及价格范围?']
DEBUG:__main__:Response type is <class 'list'>
DEBUG:__main__:Publishing message: 我有兴趣从您的经销商购买一辆使用的汽车,请给我一些关于汽车的信息,如它的制作和模型,生产年份,任何特殊的功能或选项,以及价格范围? as role: assistant to Redis
WARNING:root:Unable to read response, speaker language zh is not supported for TTS
DEBUG:__main__:Detected language zh with probability 0.9815714955329895 other potential languages: {'en': 0.0031479692552238703, 'zh': 0.9815714955329895, 'de': 0.0002693832211662084, 'es': 0.0005787646514363587, 'ru': 6.558554014191031e-05, 'ko': 0.0022140282671898603, 'fr': 0.00032671057851985097, 'ja': 0.0006878023268654943, 'pt': 0.0004050644929520786, 'tr': 0.0002767272526398301, 'pl': 0.0004122838727198541, 'ca': 8.023684472391324e-07, 'nl': 1.6140011211973615e-05, 'ar': 0.0002669195528142154, 'sv': 2.144105383194983e-05, 'it': 0.00029281957540661097, 'id': 0.0005833440227434039, 'hi': 0.0002094799856422469, 'fi': 9.646320904721506e-06, 'vi': 0.0006237156339921057, 'he': 1.4032108310857438e-06, 'uk': 4.508674464887008e-06, 'el': 2.2913016437087208e-05, 'ms': 0.0008057758677750826, 'cs': 1.215342399518704e-05, 'ro': 2.8033215130562894e-05, 'da': 6.209776984178461e-06, 'hu': 1.4816600014455616e-05, 'ta': 1.979698754439596e-05, 'no': 1.3538490293285577e-06, 'th': 0.0004379599413368851, 'ur': 8.964180597104132e-05, 'hr': 5.753419145548833e-07, 'bg': 6.132355565569014e-07, 'lt': 6.110384731528029e-08, 'la': 0.0002548990596551448, 'mi': 1.8757518773782067e-05, 'ml': 1.1129010090371594e-05, 'cy': 0.0005453431513160467, 'sk': 1.2008572412014473e-06, 'te': 2.8693079002550803e-05, 'fa': 2.4318798750755377e-05, 'lv': 8.981297838772662e-08, 'bn': 1.541602614452131e-05, 'sr': 4.462413016881328e-07, 'az': 6.566056640622264e-07, 'sl': 1.6674223388690734e-06, 'kn': 1.4236188405902794e-07, 'et': 8.859241518166527e-08, 'mk': 1.7700815035937012e-08, 'br': 4.0031613025348634e-05, 'eu': 2.812081220326945e-06, 'is': 1.7494737392098614e-07, 'hy': 2.3155772055361012e-07, 'ne': 6.247466899367282e-06, 'mn': 1.4524410289595835e-05, 'bs': 7.783343676237564e-07, 'kk': 2.4912174012570176e-07, 'sq': 4.669596265216569e-08, 'sw': 4.672059731092304e-06, 'gl': 1.8525590348872356e-05, 'mr': 2.3416684769017593e-07, 'pa': 2.8959405540263106e-07, 'si': 4.777828507940285e-05, 'km': 0.00019238001550547779, 'sn': 6.117449083831161e-05, 'yo': 2.1913141608820297e-05, 'so': 1.582882269701713e-08, 'af': 4.5264829395819106e-07, 'oc': 3.7366892229329096e-06, 'ka': 1.525216042352895e-08, 'be': 5.190613023842161e-07, 'tg': 1.6552803572267294e-09, 'sd': 5.758400675404118e-06, 'gu': 3.3124397447181764e-08, 'am': 8.855300492882634e-09, 'yi': 6.422866931643512e-07, 'lo': 7.909967280284036e-06, 'uz': 6.531064578041423e-11, 'fo': 1.816468284232542e-06, 'ht': 6.296712399489479e-06, 'ps': 1.2259225457000866e-07, 'tk': 6.665714646914012e-10, 'nn': 0.0028918865136802197, 'mt': 5.817406290020699e-08, 'sa': 4.308475399739109e-05, 'lb': 7.393896606089356e-10, 'my': 9.134150604950264e-05, 'bo': 1.9505050659063272e-05, 'tl': 8.396289922529832e-05, 'mg': 1.1652145914808898e-10, 'as': 1.359357952424034e-06, 'tt': 1.826459677944925e-10, 'haw': 0.0003064470656681806, 'ln': 2.0007398404686683e-07, 'ha': 3.1961167046290484e-10, 'ba': 5.231680089146096e-10, 'jw': 0.0017939633689820766, 'su': 3.278883831114854e-09}
DEBUG:__main__:The detected langauge zh is different from the target language en
DEBUG:__main__:In translate function
DEBUG:__main__:In colorize_transcription, transcription is: [{'spk_id': 1, 'text': ' I want to go to Paris to travel, can you help me?', 'lang': 'zh'}]
DEBUG:__main__:Result is: [{'spk_id': 1, 'text': ' I want to go to Paris to travel, can you help me?', 'lang': 'zh', 'color': 'bright_blue'}]
DEBUG:__main__:colorized_transcriptions_list: [{'spk_id': 1, 'text': ' I want to go to Paris to travel, can you help me?', 'lang': 'zh', 'color': 'bright_blue'}]
DEBUG:__main__:color is: bright_blue
DEBUG:__main__:Publishing message: (zh)->(en)  I want to go to Paris to travel, can you help me? as role: user to Redis
[94m I want to go to Paris to travel, can you help me?[0m
DEBUG:__main__:Prompt is:  I want to go to Paris to travel, can you help me?
DEBUG:__main__:Translating output from en to zh
DEBUG:__main__:Original response is 
I'm sorry, but as an AI language model, I don't have the ability to book flights or make reservations. However, I can provide you with information about Paris and its attractions so that you can make an informed decision about whether it is a place you would like to visit.
GPT RESPONSE (en-->zh): ['我很抱歉,但作为一个AI语言模型,我没有机会预订航班或预订,但是,我可以为您提供关于巴黎和其景点的信息,以便您可以做出关于它是否是一个你想参观的地方的有信息的决定。']
DEBUG:__main__:Response type is <class 'list'>
DEBUG:__main__:Publishing message: 我很抱歉,但作为一个AI语言模型,我没有机会预订航班或预订,但是,我可以为您提供关于巴黎和其景点的信息,以便您可以做出关于它是否是一个你想参观的地方的有信息的决定。 as role: assistant to Redis
WARNING:root:Unable to read response, speaker language zh is not supported for TTS
DEBUG:__main__:Detected language zh with probability 0.981702446937561 other potential languages: {'en': 0.004669144283980131, 'zh': 0.981702446937561, 'de': 0.00128113420214504, 'es': 0.00013667595339938998, 'ru': 0.00014449878653977066, 'ko': 0.0029132117051631212, 'fr': 0.0004091620503459126, 'ja': 0.0011007917346432805, 'pt': 0.0002895809302572161, 'tr': 0.00010361617023590952, 'pl': 0.00024095272237900645, 'ca': 7.650530164937663e-07, 'nl': 2.7384006898500957e-05, 'ar': 0.00021712449961341918, 'sv': 1.8474001990398392e-05, 'it': 6.720605597365648e-05, 'id': 0.00015493352839257568, 'hi': 0.0001581110991537571, 'fi': 4.739396899822168e-06, 'vi': 0.00042632551048882306, 'he': 9.242578471457819e-07, 'uk': 3.5844886951963417e-06, 'el': 2.2157544208312174e-06, 'ms': 0.0003759268147405237, 'cs': 9.920563570631202e-06, 'ro': 8.195466762117576e-06, 'da': 4.737223207484931e-06, 'hu': 1.613874701433815e-05, 'ta': 9.520472303847782e-06, 'no': 2.3408456399920397e-06, 'th': 0.00016452622367069125, 'ur': 6.077233047108166e-05, 'hr': 2.735795305852662e-07, 'bg': 5.074329010312795e-07, 'lt': 5.291184024258655e-08, 'la': 0.0003908617654815316, 'mi': 1.666377102083061e-05, 'ml': 2.2676496882922947e-05, 'cy': 0.0005366907571442425, 'sk': 5.696527978216182e-07, 'te': 1.0010011465055868e-05, 'fa': 1.0222502169199288e-05, 'lv': 7.65624861287506e-08, 'bn': 6.525489425257547e-06, 'sr': 2.1830224739005644e-07, 'az': 2.4218118710450653e-07, 'sl': 1.059055534824438e-06, 'kn': 4.0515942600904964e-08, 'et': 6.429843324440299e-08, 'mk': 9.015705515480477e-09, 'br': 4.0496921428712085e-05, 'eu': 1.7128998024418252e-06, 'is': 9.044196502827617e-08, 'hy': 1.9141945983847108e-07, 'ne': 2.136790044460213e-06, 'mn': 1.4888355508446693e-05, 'bs': 4.1947481577153667e-07, 'kk': 1.4242040435874515e-07, 'sq': 3.7333506952563766e-08, 'sw': 1.759468432283029e-06, 'gl': 7.4653385127021465e-06, 'mr': 2.483967307398416e-07, 'pa': 1.4596892583540466e-07, 'si': 2.1039160856162198e-05, 'km': 0.0001876738533610478, 'sn': 3.182325235684402e-05, 'yo': 5.203109594731359e-06, 'so': 3.5004470433364077e-09, 'af': 3.305013080989738e-07, 'oc': 2.2578560674446635e-06, 'ka': 5.739306807583944e-09, 'be': 5.157370424058172e-07, 'tg': 5.259583879535512e-10, 'sd': 1.5063803857628955e-06, 'gu': 2.01302015057081e-08, 'am': 3.749018873122623e-09, 'yi': 5.847952024851111e-07, 'lo': 2.0566326384141576e-06, 'uz': 2.4898061043443498e-11, 'fo': 1.6993494682537857e-06, 'ht': 2.230095788036124e-06, 'ps': 9.596129046940405e-08, 'tk': 2.2332156957016736e-10, 'nn': 0.0027875364758074284, 'mt': 3.0366635428435984e-08, 'sa': 3.24748398270458e-05, 'lb': 4.2142650480414545e-10, 'my': 2.9694769182242453e-05, 'bo': 1.0529501196288038e-05, 'tl': 4.428023748914711e-05, 'mg': 3.638406936845584e-11, 'as': 3.7320569390431046e-07, 'tt': 6.91307497358018e-11, 'haw': 0.00018222755170427263, 'ln': 5.3794920518157596e-08, 'ha': 9.224305347332873e-11, 'ba': 1.7402189411708235e-10, 'jw': 0.0008643327746540308, 'su': 6.919343986666604e-10}
DEBUG:__main__:The detected langauge zh is different from the target language en
DEBUG:__main__:In translate function
DEBUG:__main__:In colorize_transcription, transcription is: [{'spk_id': 1, 'text': ' I plan to leave from Fenghuangcheng', 'lang': 'zh'}]
DEBUG:__main__:Result is: [{'spk_id': 1, 'text': ' I plan to leave from Fenghuangcheng', 'lang': 'zh', 'color': 'bright_blue'}]
DEBUG:__main__:colorized_transcriptions_list: [{'spk_id': 1, 'text': ' I plan to leave from Fenghuangcheng', 'lang': 'zh', 'color': 'bright_blue'}]
DEBUG:__main__:color is: bright_blue
DEBUG:__main__:Publishing message: (zh)->(en)  I plan to leave from Fenghuangcheng as role: user to Redis
[94m I plan to leave from Fenghuangcheng[0m
DEBUG:__main__:Prompt is:  I plan to leave from Fenghuangcheng
DEBUG:__main__:Translating output from en to zh
DEBUG:__main__:Original response is  in the morning and will be back in Shanghai by the evening.
I am wondering if there are any good places to eat around Fenghuangcheng? Is there a local food culture that is worth experiencing?
GPT RESPONSE (en-->zh): ['早上,我会在晚上回到上海,我想知道有没有在福恩山周围吃的好地方吗?有当地的食物文化值得体验吗?']
DEBUG:__main__:Response type is <class 'list'>
DEBUG:__main__:Publishing message: 早上,我会在晚上回到上海,我想知道有没有在福恩山周围吃的好地方吗?有当地的食物文化值得体验吗? as role: assistant to Redis
WARNING:root:Unable to read response, speaker language zh is not supported for TTS
DEBUG:__main__:Detected language zh with probability 0.9975419044494629 other potential languages: {'en': 0.0008272124687209725, 'zh': 0.9975419044494629, 'de': 1.9915629309252836e-05, 'es': 2.230321115348488e-05, 'ru': 9.687570127425715e-06, 'ko': 0.000343546736985445, 'fr': 1.9477080059004948e-05, 'ja': 0.0001582365221111104, 'pt': 2.7311252779327333e-05, 'tr': 2.614427103253547e-05, 'pl': 2.980710814881604e-05, 'ca': 1.994867382393295e-08, 'nl': 2.22222456613963e-06, 'ar': 2.8297070457483642e-05, 'sv': 3.84176246370771e-06, 'it': 1.1500522305141203e-05, 'id': 3.0844283173792064e-05, 'hi': 2.659349047462456e-05, 'fi': 4.7360390453832224e-07, 'vi': 3.920253584510647e-05, 'he': 3.6879963971614416e-08, 'uk': 2.510194292426604e-07, 'el': 3.3187379244736803e-07, 'ms': 4.388457819004543e-05, 'cs': 3.030775701517996e-07, 'ro': 6.590047405552468e-07, 'da': 1.5436611988661753e-07, 'hu': 7.251217084558448e-07, 'ta': 1.0774349448183784e-06, 'no': 8.704568443818061e-08, 'th': 2.8859089070465416e-05, 'ur': 6.377204954333138e-06, 'hr': 1.718404263328921e-08, 'bg': 3.4343273114245676e-08, 'lt': 1.8426146164429724e-09, 'la': 2.8318128897808492e-05, 'mi': 6.33711579212104e-07, 'ml': 2.341148046980379e-06, 'cy': 6.77617426845245e-05, 'sk': 2.7987153927711006e-08, 'te': 3.244551862735534e-06, 'fa': 7.478021188944695e-07, 'lv': 1.8992463157729844e-09, 'bn': 4.5181127461546566e-07, 'sr': 9.317088434102061e-09, 'az': 2.6367681371652907e-08, 'sl': 5.5501889306697194e-08, 'kn': 4.293623234730148e-09, 'et': 2.553240063818407e-09, 'mk': 4.5003711868218943e-10, 'br': 2.6035227165266406e-06, 'eu': 7.350169539677154e-08, 'is': 5.5576436785997885e-09, 'hy': 5.946785286425893e-09, 'ne': 1.5370726202945661e-07, 'mn': 6.225322408681677e-07, 'bs': 2.7422652593145358e-08, 'kk': 6.367082860947448e-09, 'sq': 1.4330248099270193e-09, 'sw': 1.5635980332717736e-07, 'gl': 3.141788340599305e-07, 'mr': 1.1008805422818568e-08, 'pa': 1.4869848463661128e-08, 'si': 2.6450343284523115e-06, 'km': 1.4269346138462424e-05, 'sn': 4.3700124479073565e-06, 'yo': 1.1449901649029925e-06, 'so': 2.2524990206385098e-10, 'af': 2.034197166267404e-08, 'oc': 1.6302462313433352e-07, 'ka': 2.0918373977441007e-10, 'be': 1.8234947773976273e-08, 'tg': 2.4909825938057573e-11, 'sd': 1.900563546541889e-07, 'gu': 8.846021692932027e-10, 'am': 1.2978954022635492e-10, 'yi': 3.59032661378933e-08, 'lo': 2.260197362602412e-07, 'uz': 1.259337686215778e-12, 'fo': 1.509305036506703e-07, 'ht': 2.3640853896722547e-07, 'ps': 4.167837630575377e-09, 'tk': 1.3535567632005918e-11, 'nn': 0.0004703149024862796, 'mt': 2.5255981750405e-09, 'sa': 3.202772404620191e-06, 'lb': 9.034862268053612e-12, 'my': 2.5260330858145608e-06, 'bo': 6.562177645719203e-07, 'tl': 8.318030268128496e-06, 'mg': 1.6425236821701605e-12, 'as': 4.557786681402831e-08, 'tt': 2.7817752441816612e-12, 'haw': 2.689911525521893e-05, 'ln': 3.3622127304511196e-09, 'ha': 5.328429537876378e-12, 'ba': 1.144545222486748e-11, 'jw': 0.00010563930118223652, 'su': 2.572982972515181e-11}
DEBUG:__main__:The detected langauge zh is different from the target language en
DEBUG:__main__:In translate function
DEBUG:__main__:In colorize_transcription, transcription is: [{'spk_id': 4, 'text': ' Can you help me find the best airline company?', 'lang': 'zh'}]
DEBUG:__main__:Result is: [{'spk_id': 4, 'text': ' Can you help me find the best airline company?', 'lang': 'zh', 'color': 'deep_pink1'}]
DEBUG:__main__:colorized_transcriptions_list: [{'spk_id': 4, 'text': ' Can you help me find the best airline company?', 'lang': 'zh', 'color': 'deep_pink1'}]
DEBUG:__main__:color is: deep_pink1
DEBUG:__main__:Publishing message: (zh)->(en)  Can you help me find the best airline company? as role: user to Redis
[35m Can you help me find the best airline company?[0m
DEBUG:__main__:Prompt is:  Can you help me find the best airline company?
DEBUG:__main__:Translating output from en to zh
DEBUG:__main__:Original response is 
GPT RESPONSE (en-->zh): ['此分類上一篇']
DEBUG:__main__:Response type is <class 'list'>
DEBUG:__main__:Publishing message: 此分類上一篇 as role: assistant to Redis
WARNING:root:Unable to read response, speaker language zh is not supported for TTS
DEBUG:__main__:Detected language zh with probability 0.9921091198921204 other potential languages: {'en': 0.0022130042780190706, 'zh': 0.9921091198921204, 'de': 0.00040206979610957205, 'es': 0.0001463163353037089, 'ru': 8.140593854477629e-05, 'ko': 0.0005393038736656308, 'fr': 0.00013265102461446077, 'ja': 0.00036111558438278735, 'pt': 0.0001521260419394821, 'tr': 5.686666554538533e-05, 'pl': 7.018969336058944e-05, 'ca': 2.669934815457964e-07, 'nl': 6.549599220306845e-06, 'ar': 9.838045662036166e-05, 'sv': 9.994568245019764e-06, 'it': 0.00010940960783045739, 'id': 7.133419421734288e-05, 'hi': 7.52052292227745e-05, 'fi': 4.60777482658159e-06, 'vi': 0.0007874757284298539, 'he': 2.990062455410225e-07, 'uk': 1.9244771465309896e-06, 'el': 2.19533103518188e-06, 'ms': 0.00015385235019493848, 'cs': 4.423185146151809e-06, 'ro': 4.452633220353164e-06, 'da': 2.9671684842469404e-06, 'hu': 1.085147505364148e-05, 'ta': 5.193244760448579e-06, 'no': 5.501564714904816e-07, 'th': 0.0001783643092494458, 'ur': 5.999635686748661e-05, 'hr': 1.8683444125144888e-07, 'bg': 1.1923845022465684e-07, 'lt': 2.436783930193087e-08, 'la': 0.00013463155482895672, 'mi': 7.185518370533828e-06, 'ml': 1.2789637366950046e-05, 'cy': 0.00026680779410526156, 'sk': 2.886359027343133e-07, 'te': 9.993625099014025e-06, 'fa': 5.120626155985519e-06, 'lv': 4.717198009984713e-08, 'bn': 4.63473770651035e-06, 'sr': 1.3298762269187137e-07, 'az': 2.160892620395316e-07, 'sl': 5.459912699734559e-07, 'kn': 3.0903407832738594e-08, 'et': 3.022463346269433e-08, 'mk': 4.849847190513401e-09, 'br': 1.8013795852311887e-05, 'eu': 1.06197546756448e-06, 'is': 5.008565651110075e-08, 'hy': 6.879064784470756e-08, 'ne': 1.8845727254301892e-06, 'mn': 4.47379215984256e-06, 'bs': 3.10360064759152e-07, 'kk': 8.649421090467513e-08, 'sq': 2.08673398560677e-08, 'sw': 1.335592628493032e-06, 'gl': 9.543962733005174e-06, 'mr': 8.226538739108946e-08, 'pa': 1.1240925346100994e-07, 'si': 1.219223122461699e-05, 'km': 6.572165148099884e-05, 'sn': 2.3754026187816635e-05, 'yo': 4.811300641449634e-06, 'so': 4.428141853196621e-09, 'af': 1.022726081600922e-07, 'oc': 1.5406420743602212e-06, 'ka': 2.911100471791883e-09, 'be': 4.5592832975671627e-07, 'tg': 2.8281019193165946e-10, 'sd': 1.7618596075408277e-06, 'gu': 1.0834075858667802e-08, 'am': 1.4531390535310607e-09, 'yi': 3.625449949140602e-07, 'lo': 2.073194309559767e-06, 'uz': 8.723445577007993e-12, 'fo': 1.0901101177296368e-06, 'ht': 1.3874118849344086e-06, 'ps': 3.858415809077087e-08, 'tk': 1.205075483845519e-10, 'nn': 0.0009510373347438872, 'mt': 1.3424332756528656e-08, 'sa': 2.7556703571463004e-05, 'lb': 1.1451546655383282e-10, 'my': 4.766623169416562e-05, 'bo': 1.0813902008521836e-05, 'tl': 2.0743620552821085e-05, 'mg': 1.7647576108781315e-11, 'as': 4.60873934571282e-07, 'tt': 3.562712624916031e-11, 'haw': 0.00010369683877797797, 'ln': 3.225395062145253e-08, 'ha': 4.5904953449582564e-11, 'ba': 9.558712849022655e-11, 'jw': 0.00039044860750436783, 'su': 2.614439498227483e-10}
DEBUG:__main__:The detected langauge zh is different from the target language en
DEBUG:__main__:In translate function
DEBUG:__main__:In colorize_transcription, transcription is: [{'spk_id': 1, 'text': ' If I want to avoid traveling, high-speed trains and any extreme weather', 'lang': 'zh'}]
DEBUG:__main__:Result is: [{'spk_id': 1, 'text': ' If I want to avoid traveling, high-speed trains and any extreme weather', 'lang': 'zh', 'color': 'bright_blue'}]
DEBUG:__main__:colorized_transcriptions_list: [{'spk_id': 1, 'text': ' If I want to avoid traveling, high-speed trains and any extreme weather', 'lang': 'zh', 'color': 'bright_blue'}]
DEBUG:__main__:color is: bright_blue
DEBUG:__main__:Publishing message: (zh)->(en)  If I want to avoid traveling, high-speed trains and any extreme weather as role: user to Redis
[94m If I want to avoid traveling, high-speed trains and any extreme weather[0m
DEBUG:__main__:Prompt is:  If I want to avoid traveling, high-speed trains and any extreme weather
DEBUG:__main__:Translating output from en to zh
DEBUG:__main__:Original response is  conditions.
I would like to know if there are any plans for a high-speed train between New York City and Washington D.C.?
GPT RESPONSE (en-->zh): ['我想知道是否有任何计划在纽约市和华盛顿市之间的高速列车?']
DEBUG:__main__:Response type is <class 'list'>
DEBUG:__main__:Publishing message: 我想知道是否有任何计划在纽约市和华盛顿市之间的高速列车? as role: assistant to Redis
WARNING:root:Unable to read response, speaker language zh is not supported for TTS
DEBUG:__main__:Detected language zh with probability 0.998624324798584 other potential languages: {'en': 0.00027492709341458976, 'zh': 0.998624324798584, 'de': 1.1863316103699617e-05, 'es': 1.4167231711326167e-05, 'ru': 7.18320598025457e-06, 'ko': 0.00013705009769182652, 'fr': 3.2100385851663304e-06, 'ja': 0.0001286896876990795, 'pt': 8.36747949506389e-06, 'tr': 6.885369657538831e-06, 'pl': 7.850825568311848e-06, 'ca': 1.0804622974092126e-08, 'nl': 1.1173974598932546e-06, 'ar': 1.155962763732532e-05, 'sv': 5.714574626836111e-07, 'it': 6.834928626631154e-06, 'id': 1.587714177730959e-05, 'hi': 5.302284989738837e-06, 'fi': 2.844602420282172e-07, 'vi': 5.608391802525148e-05, 'he': 1.0108754722182312e-08, 'uk': 1.2574162155942759e-07, 'el': 2.1997300336806802e-07, 'ms': 3.0116536436253227e-05, 'cs': 2.75602104693462e-07, 'ro': 2.39370308463549e-07, 'da': 1.012278687539947e-07, 'hu': 5.297742973198183e-07, 'ta': 8.250313499047479e-07, 'no': 3.549456195628409e-08, 'th': 4.1342073018313386e-06, 'ur': 4.7580078899045475e-06, 'hr': 1.3769385631690056e-08, 'bg': 1.1424085677447238e-08, 'lt': 8.503512338720043e-10, 'la': 2.7845328077091835e-05, 'mi': 4.0776163245936914e-07, 'ml': 2.337719251954695e-06, 'cy': 3.585593367461115e-05, 'sk': 2.2743702032812507e-08, 'te': 1.0638391358952504e-06, 'fa': 1.5092923888460064e-07, 'lv': 2.036508073288701e-09, 'bn': 3.3974109214796044e-07, 'sr': 3.6940530634410607e-09, 'az': 9.159765390620578e-09, 'sl': 2.4679392751636442e-08, 'kn': 2.219104233702751e-09, 'et': 1.5827975596849342e-09, 'mk': 2.11072478939478e-10, 'br': 1.8629409623827087e-06, 'eu': 3.967453565678625e-08, 'is': 5.480981002392582e-09, 'hy': 1.2151202266608152e-09, 'ne': 7.703434334871417e-08, 'mn': 4.811089979739336e-07, 'bs': 1.0203304867673069e-08, 'kk': 4.398417186024517e-09, 'sq': 6.075610015088273e-10, 'sw': 8.035047471821599e-08, 'gl': 6.445591225201497e-07, 'mr': 4.920274854214313e-09, 'pa': 6.49354925386092e-09, 'si': 1.987602445296943e-06, 'km': 8.817850357445423e-06, 'sn': 1.939257572303177e-06, 'yo': 3.232274821129977e-07, 'so': 2.017997435821428e-10, 'af': 1.950573569331482e-08, 'oc': 1.2138983151999128e-07, 'ka': 1.0878102585376581e-10, 'be': 1.409709948774207e-08, 'tg': 9.587041230330051e-12, 'sd': 1.22796720347651e-07, 'gu': 2.6452715018443484e-10, 'am': 4.8563104926291345e-11, 'yi': 2.135468868402768e-08, 'lo': 6.75060363164448e-08, 'uz': 5.730525646022167e-13, 'fo': 1.3859214220701688e-07, 'ht': 7.347556874037764e-08, 'ps': 1.4178366258832398e-09, 'tk': 7.674498189724765e-12, 'nn': 0.00039870713953860104, 'mt': 9.833082126320392e-10, 'sa': 3.382802560736309e-06, 'lb': 5.26951225710004e-12, 'my': 3.6594158245861763e-06, 'bo': 7.182119929893815e-07, 'tl': 3.27529323840281e-06, 'mg': 8.241025049871009e-13, 'as': 2.0407513900977392e-08, 'tt': 2.3212722976423406e-12, 'haw': 2.46582567342557e-05, 'ln': 9.23716769740679e-10, 'ha': 2.231643472447309e-12, 'ba': 6.293886418984318e-12, 'jw': 0.0001170783507404849, 'su': 1.766824533899758e-11}
DEBUG:__main__:The detected langauge zh is different from the target language en
DEBUG:__main__:In translate function
DEBUG:__main__:In colorize_transcription, transcription is: [{'spk_id': 6, 'text': ' When is the best time to travel?', 'lang': 'zh'}]
DEBUG:__main__:Result is: [{'spk_id': 6, 'text': ' When is the best time to travel?', 'lang': 'zh', 'color': 'magenta'}]
DEBUG:__main__:colorized_transcriptions_list: [{'spk_id': 6, 'text': ' When is the best time to travel?', 'lang': 'zh', 'color': 'magenta'}]
DEBUG:__main__:color is: magenta
DEBUG:__main__:Publishing message: (zh)->(en)  When is the best time to travel? as role: user to Redis
[35m When is the best time to travel?[0m
DEBUG:__main__:Prompt is:  When is the best time to travel?
DEBUG:__main__:Translating output from en to zh
DEBUG:__main__:Original response is 
When is the best time to travel depends on what you want to do and where you want to go. Generally, the best time to travel is during the low season in a particular destination. This means that the weather is more pleasant, flights are cheaper, and accommodations are less crowded. However, if you enjoy warm weather and crowds, then traveling during peak season can be ideal. For example, if you want to visit Hawaii during the winter months, it's best to book your trip well in advance as prices are higher due to high demand.
GPT RESPONSE (en-->zh): ['旅行的最佳时间是什么时候取决于你想做什么,你想去哪里。 一般来说,旅行的最佳时间是在某个目的地的低季节期间。 这意味着天气更愉快,航班更便宜,住宿更少繁忙。 但是,如果你享受温暖的天气和人群,那么在峰季期间旅行可以是理想的。 例如,如果你想在冬季访问夏威夷,最好提前预订你的旅行,因为价格高,因为需求高。']
DEBUG:__main__:Response type is <class 'list'>
DEBUG:__main__:Publishing message: 旅行的最佳时间是什么时候取决于你想做什么,你想去哪里。 一般来说,旅行的最佳时间是在某个目的地的低季节期间。 这意味着天气更愉快,航班更便宜,住宿更少繁忙。 但是,如果你享受温暖的天气和人群,那么在峰季期间旅行可以是理想的。 例如,如果你想在冬季访问夏威夷,最好提前预订你的旅行,因为价格高,因为需求高。 as role: assistant to Redis
WARNING:root:Unable to read response, speaker language zh is not supported for TTS
DEBUG:__main__:Detected language nn with probability 0.7119759917259216 other potential languages: {'en': 0.11885383725166321, 'zh': 0.007230507209897041, 'de': 0.0060289171524345875, 'es': 0.007105162832885981, 'ru': 0.030244162306189537, 'ko': 0.03432280570268631, 'fr': 0.010683021508157253, 'ja': 0.019037500023841858, 'pt': 0.004266263451427221, 'tr': 0.005251714028418064, 'pl': 0.0024797574151307344, 'ca': 7.391779945464805e-05, 'nl': 0.001141623710282147, 'ar': 0.0009429040946997702, 'sv': 0.000541704474017024, 'it': 0.002653478877618909, 'id': 0.0008060488034971058, 'hi': 0.002872089622542262, 'fi': 0.0006116355652920902, 'vi': 0.0019330482464283705, 'he': 5.139278437127359e-05, 'uk': 0.00047275208635255694, 'el': 0.00031294961809180677, 'ms': 0.004691767040640116, 'cs': 0.0006739171803928912, 'ro': 0.000810199708212167, 'da': 0.00027138160658068955, 'hu': 0.0006382552091963589, 'ta': 0.001178967417217791, 'no': 0.0002743840159382671, 'th': 0.0007109455764293671, 'ur': 0.0008330969722010195, 'hr': 6.51053196634166e-05, 'bg': 8.683875785209239e-05, 'lt': 7.9891542554833e-06, 'la': 0.005310656037181616, 'mi': 0.00032513844780623913, 'ml': 0.0011126953177154064, 'cy': 0.0035024185199290514, 'sk': 9.22976469155401e-05, 'te': 0.00033277494367212057, 'fa': 0.00018660983187146485, 'lv': 1.0045445378636941e-05, 'bn': 0.00018696770712267607, 'sr': 1.5790912584634498e-05, 'az': 1.345779855910223e-05, 'sl': 5.856039933860302e-05, 'kn': 5.047593731433153e-06, 'et': 1.301027623412665e-05, 'mk': 1.6790888821560657e-06, 'br': 0.000199960995814763, 'eu': 2.100293932016939e-05, 'is': 1.2179333680251148e-05, 'hy': 6.438306627387647e-06, 'ne': 3.2548821764066815e-05, 'mn': 0.0004062703810632229, 'bs': 6.071631651138887e-05, 'kk': 4.595246537064668e-06, 'sq': 2.6615189199219458e-06, 'sw': 3.383951843716204e-05, 'gl': 0.00014281357289291918, 'mr': 6.3959264480217826e-06, 'pa': 4.0079116843116935e-06, 'si': 0.0002508964971639216, 'km': 0.0005204972112551332, 'sn': 0.000279790663626045, 'yo': 3.748122981050983e-05, 'so': 1.4011148152803798e-07, 'af': 2.945270352938678e-05, 'oc': 2.410861816315446e-05, 'ka': 2.0967504497093614e-06, 'be': 1.2863326446677092e-05, 'tg': 2.3879985988628505e-08, 'sd': 1.740137486194726e-05, 'gu': 1.0539786217123037e-06, 'am': 2.2449363257237565e-07, 'yi': 7.471108801837545e-06, 'lo': 8.63205968926195e-06, 'uz': 6.151898990225391e-10, 'fo': 9.810931805986911e-05, 'ht': 2.624704211484641e-05, 'ps': 5.177050752536161e-06, 'tk': 5.016776327693151e-09, 'nn': 0.7119759917259216, 'mt': 6.392008344846545e-07, 'sa': 0.00019624567357823253, 'lb': 1.0916945569761083e-08, 'my': 3.87095678888727e-05, 'bo': 5.8323195844423026e-05, 'tl': 0.0004075747274328023, 'mg': 7.670076240806623e-10, 'as': 2.143016899935901e-06, 'tt': 5.477284847899e-09, 'haw': 0.0008501491392962635, 'ln': 1.0816537496793899e-06, 'ha': 2.832357681725739e-09, 'ba': 3.871698517343702e-09, 'jw': 0.004886730574071407, 'su': 2.409869814812282e-08}
DEBUG:__main__:The detected langauge nn is different from the target language en
DEBUG:__main__:In translate function
DEBUG:__main__:In colorize_transcription, transcription is: [{'spk_id': 2, 'text': ' The sentence may be cut off, do not make up words to fill in the rest of the sentence', 'lang': 'nn'}]
DEBUG:__main__:Result is: [{'spk_id': 2, 'text': ' The sentence may be cut off, do not make up words to fill in the rest of the sentence', 'lang': 'nn', 'color': 'bright_green'}]
DEBUG:__main__:colorized_transcriptions_list: [{'spk_id': 2, 'text': ' The sentence may be cut off, do not make up words to fill in the rest of the sentence', 'lang': 'nn', 'color': 'bright_green'}]
DEBUG:__main__:color is: bright_green
DEBUG:__main__:Publishing message: (nn)->(en)  The sentence may be cut off, do not make up words to fill in the rest of the sentence as role: user to Redis
[92m The sentence may be cut off, do not make up words to fill in the rest of the sentence[0m
DEBUG:__main__:Prompt is:  The sentence may be cut off, do not make up words to fill in the rest of the sentence
DEBUG:__main__:Translating output from en to nn
DEBUG:__main__:Original response is .
I'm sorry, but I cannot complete this task as it goes against OpenAI's content policy on generating inappropriate or harmful language.
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/diart/sources.py", line 192, in read
    self.stream.on_next(self._queue.get_nowait())
  File "/usr/local/lib/python3.10/dist-packages/rx/subject/subject.py", line 55, in on_next
    super().on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/observer.py", line 26, in on_next
    self._on_next_core(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/subject/subject.py", line 62, in _on_next_core
    observer.on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/map.py", line 41, in on_next
    obv.on_next(result)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/filter.py", line 34, in on_next
    observer.on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/filter.py", line 34, in on_next
    observer.on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/map.py", line 41, in on_next
    obv.on_next(result)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/map.py", line 41, in on_next
    obv.on_next(result)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/windowwithcount.py", line 61, in on_next
    s.on_completed()
  File "/usr/local/lib/python3.10/dist-packages/rx/subject/subject.py", line 89, in on_completed
    super().on_completed()
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/observer.py", line 56, in on_completed
    self._on_completed_core()
  File "/usr/local/lib/python3.10/dist-packages/rx/subject/subject.py", line 97, in _on_completed_core
    observer.on_completed()
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 44, in on_completed
    self._on_completed()
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 44, in on_completed
    self._on_completed()
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/toiterable.py", line 24, in on_completed
    observer.on_next(queue)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/map.py", line 41, in on_next
    obv.on_next(result)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/internal/concurrency.py", line 16, in inner
    return fn(*args, **kw)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/filter.py", line 34, in on_next
    observer.on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/map.py", line 41, in on_next
    obv.on_next(result)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/map.py", line 41, in on_next
    obv.on_next(result)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/filter.py", line 34, in on_next
    observer.on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/map.py", line 41, in on_next
    obv.on_next(result)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/operators/map.py", line 41, in on_next
    obv.on_next(result)
  File "/usr/local/lib/python3.10/dist-packages/rx/core/observer/autodetachobserver.py", line 26, in on_next
    self._on_next(value)
  File "/usr/app/src/diart_whisper.py", line 243, in respond_and_print
    output = translate_text(output, target_lang, lang)
  File "/usr/app/src/diart_whisper.py", line 149, in translate_text
    raise ValueError(f"Unsupported langauge. Requesting translation from {src_lang} (supported:{src_supported}) to {target_lang} (supported:{target_supported})")
ValueError: Unsupported langauge. Requesting translation from en (supported:True) to nn (supported:False)
INFO:__main__:Starting translation and captioning, begin speaking...
DEBUG:__main__:Closing audio stream
Unexpected exception occurred: Error starting stream: Invalid stream pointer [PaErrorCode -9988]
[?2004h]0;openvino@ac1ac0ba9dd5: /usr/app/srcopenvino@ac1ac0ba9dd5:/usr/app/src$ clear
[?2004l
[H[2J[3J[?2004h]0;
```