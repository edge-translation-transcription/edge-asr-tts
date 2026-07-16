# Benchmarking
The ansible playbook installs metrics and dashboard to track the utilization of both the host system(s) and container(s). Components include:

1. [Grafana](https://grafana.com)
2. [Prometheus](https://prometheus.io/)
3. [cAdvisor](https://github.com/google/cadvisor) 
4. [cAdvisor Dashboard](https://grafana.com/api/dashboards/15798/revisions/12/download)
5. [node_exporter Dashboard](https://grafana.com/api/dashboards/1860/revisions/37/download)

You can view the collected metrics graph at the url by opening a browser on your primary host:
[http://localhost:3000](http://localhost:3000) replace localhost with the IP of your primary host if you are viewing from another system
The default username is 'admin' and the password is what you have chosen to set in the `GRAFANA_ADMIN_PASSWORD` environment variable.

[Back to main page](../../README.md)

Speaker Diarization Inifinity Dashboard:
![speaker_dashboard](https://github.com/user-attachments/assets/79169d1a-bfdd-42d7-892a-29ba4fe09753)
ASR Inifinity Dashboard:
![asr_dashboar![tts_dashboard](https://github.com/user-attachments/assets/fdcd63fe-c89c-45dc-a902-bcfe981cfea8)
d](https://github.com/user-attachments/assets/7a08d4ea-3ad4-4c5e-bc4c-da9a09f91ef5)
TTS Inifinity Dashboard:
![tts_dashboard](https://github.com/user-attachments/assets/f07d798a-8b1a-49ed-8f2f-d47cbf7094af)

Benchmarks of [hf-seamless-m4t-medium](https://huggingface.co/facebook/hf-seamless-m4t-medium) speech generation on 24 core Raptor lake 13th gen i9-13900K, 32Gb memory. 
![image](https://github.com/user-attachments/assets/739c0608-0c00-47ee-8de9-04f6dc288b3b)
-	Small ~ 5 sec of speech
-	Medium ~ 15 sec of speech
-	Large ~ 30 sec of speech
