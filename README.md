# Table of Contents

[Overview](#overview)\
[Architecture](./docs/architecture/README.md)\
[Auth Keys](#model-access-keys)\
[Deployment](#deployment)\
[Benchmarking](./docs/benchmarking/README.md)\
[Sample Output](./docs/sample_output/README.md)\
[Windows Setup](./docs/windows/README.md)

## Overview

This repository is the demonstration of an Automated Speech Recognition workload that implements:

* Speech detection
* Speaker identification
* Transcription
* Translation

The use case is for conversation between a machine and human (MTH) and between humans (HTH). All models used are open source.
They have not been trained on any additional datasets. For the purpose of MTH, we use a GPT-based chatbot.

The pipeline can be run on a resource constrained client device, and following initial setup and configuration, does not
require internet access. Resource constrained can be defined as:

* Between 4-16G RAM
* CPU-only inference
* 100-500G Storage

For additional architectural details, see [Architecure](./docs/architecure/README.md)

## Model Access Keys

You will need to have tokens/keys for:

1. [Hugging Face](https://huggingface.co/docs/api-inference/en/quicktour)
2. [Open AI](https://platform.openai.com/account/api-keys)
3. [Detect Language](https://detectlanguage.com/users/sign_up)
4. You must agree to provide your contact information to use the pyannote models on hugging face:

Accept the conditions for the pyannote models:

1. visit https://hf.co/pyannote/segmentation to accept the user conditions
2. visit https://hf.co/pyannote/embedding to accept the user conditions.
3. visit https://hf.co/pyannote/speaker-diarization to accept the user conditions.
4. visit https://hf.co/pyannote/speaker-diarization-3.1 to accept the user conditions

## Deployment

 This section covers how to configure a system for deployment of the sample ASR workload.

### Host Machine Build Prerequisites

Any host machine will need to meet the following minimum criteria.

1. PC config:
    1. Ubuntu LTS OS (this solution is validated on 22.04)
    2. At least 4G of RAM
    3. At least 250G Storage
    4. [Intel Processor Compatible with OpenVINO](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/system-requirements.html)
    5. A microphone
    6. A speaker
    7. A display
    8. Your CPU needs to support AVX or AVX2 instructions
    9. You need enough RAM to load the models into memory.
2. An admin user exists on all hosts with the same login credential
3. The admin user has sudo privileges
4. openssh-server is installed on all hosts: ```sudo apt install -y openssh-server```

For more information on why SSH is needed, see [ansible node requirements](https://docs.ansible.com/ansible/2.9/installation_guide/intro_installation.html#control-node-requirements)

### Configure Primary System

1. Choose one system to be the config server (this will be the same if you have a single machine).
2. Install git on the config host: ```sudo apt install -y git```
3. Set environment variables:
   1. GRAFANA_ADMIN_PASSWORD
   2. R4ALL_DIR 
   > **_IMPORTANT:_** Your GRAFANA_ADMIN_PASSWORD must adhere to the [Grafana Password Policy](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/grafana/#strong-password-policy) or password reset will fail.

```console
git clone https://github.com/edge-translation-transcription/edge-asr-tts.git
cd edge-asr-tts
export R4ALL_DIR=`pwd`
# REPLACE THE VARIABLE BELOW WITH THE PASSWORD YOU WANT YOUR GRAFANA ADMIN TO HAVE
export GRAFANA_ADMIN_PASSWORD='your_grafana_password' # Use single quotes so special characters are not interpreted
chmod +x base-config.sh
sudo -E ./base-config.sh # This will install the necessary packages
```

#### Create the Environment Variable File

Use your editor of choice to create a file with the environment variables that will be passed into the container
at runtime. Example (Replace the placeholder values with your real keys from the [model access keys section](#model-access-keys)):

```console
touch $HOME/r4a_secrets.env
echo "OPENAI_KEY=openai_key" > $HOME/r4a_secrets.env
echo "DETECTION_KEY=detection_key" >> $HOME/r4a_secrets.env
echo "HF_KEY=hf_key" >> $HOME/r4a_secrets.env
```

#### Add Aliases for Secondary Systems

> **_NOTE_** Only run this step if you have more than one system -- all host systems must on a network reachable by the primary system.

Add the IP addresses for hosts you intend to deploy to are in the `/etc/hosts` file, for example:

```bash
IPAddress      Hostname          Alias
127.0.0.1      localhost         host1
192.168.2.1    host1.domain.com  host1
192.168.2.2    host2.domain.com  host2
192.168.2.3    web.openna.com    host3
```

Then run: WIP -- #TODO this script has to be tested

```console
./autogen-sshkeys.exp
```

### Build the Application

You should not have to reset the variable, but if you opened a new terminal for any reason,

```export R4ALL_DIR=/path/to/r4a-github-repo``` <-- Replace with the path to your clone of this repo

> **_NOTE_**: The Dockerfile is generated from [docker_ci](https://github.com/openvinotoolkit/docker_ci.git) following the [OpenVINO Docker guide](https://github.com/openvinotoolkit/docker_ci/blob/master/docs/openvino_docker.md) and then modified. The command to generate the Dockerfile for this repo is: ```python3 docker_openvino.py gen_dockerfile -os ubuntu22 --distribution runtime --product_version 2024.5```

1. Ensure that the current user is a member of the `docker` unix group: by running the `groups` command.
    * The ansible automation will have added the `remote_user` to the group.
    * You may need to load the new group by running `newgrp docker` prior to building the image.
2. Build docker image (this step takes around 15 minutes):

    ```console
    docker build -f Dockerfile --build-arg \
   package_url=https://storage.openvinotoolkit.org/repositories/openvino/packages/2024.5/linux/l_openvino_toolkit_ubuntu22_2024.5.0.17288.7975fa5da0c_x86_64.tgz \
   --no-cache --tag=r4all:0.0.1 .
    ```
    > If you are behind a proxy, use Build args:

    ```console
    # Behind a proxy
    docker build -f Dockerfile --build-arg HTTP_PROXY=${HTTP_PROXY} --build-arg HTTPS_PROXY=${HTTPS_PROXY} --build-arg NO_PROXY=${NO_PROXY} --build-arg package_url=https://storage.openvinotoolkit.org/repositories/openvino/packages/2024.5/linux/l_openvino_toolkit_ubuntu22_2024.5.0.17288.7975fa5da0c_x86_64.tgz    --no-cache --tag=r4all:0.0.1 .
    ```

#### Edit the Application Config File

The [r4a_config.json](./r4a_config.json) contains default settings. This file will be passed to the docker run command to
and its values will be parsed by the script at runtime. For any of the key config variables, they will override the environment 
variables you set in the [create secrets file step](#create-the-environment-variable-file).

### Run Configuration Management

The configuration management will ensure that the necessary system packages and settings, Python libraries and modules, applications, and metrics gathering
are deployed on the systems in the ansible inventory file. The github repository and secrets file will be distributed to any secondary systems from the primary.

> **_NOTE_**: When prompted, `Become Password` is the password of your admin user to escalate to root

1. ```cp ansible_hosts.yaml $HOME/Documents/```
2. Edit the ```$HOME/Documents/ansible_hosts.yaml``` file to have the IP addresses of your hosts
3. Edit the `ansible-config.yaml` file, replace `remote_user` with your admin username
    * example: `hostname -I` will give you the host IP of the system you are currently logged into
4. Edit the [vars/main.yml](./vars/main.yml) file to have the pulseaudio_user be the user starting the pulse audio socket **it should NOT be root**.
5. Execute the ansible file:

```console
ansible-playbook -i $HOME/Documents/ansible_hosts.yaml ansible-config.yaml --ask-become-pass
```

## Run the Application

On any host that has been configured, you will now be able to launch the containerized ASR application.

1. Run the docker file:
```console
docker run -it --privileged --name r4all-test \
--rm -v ${R4ALL_DIR}:/usr/app/src --env \
PULSE_SERVER=unix:/tmp/pulseaudio.socket \
--env PULSE_COOKIE=/tmp/pulseaudio.cookie \
--volume /tmp/pulseaudio.socket:/tmp/pulseaudio.socket \
--volume /tmp/pulseaudio.client.conf:/etc/pulse/client.conf \
--volume /var/www/metrics:/usr/app/src/csv \
--env-file=${HOME}/r4a_secrets.env \
-p 8501:8501 \
-e DISPLAY=$DISPLAY --user openvino -w /usr/app/src \
--group-add=audio --device /dev/snd r4all:0.0.1
```
2. Currently, the app is being debugged, the file will change to run automatically in the Dockerfile, for now, at the prompt: 
```console
   ./retail_for_all.sh 
```
3. You can also run the application with a different config file by providing a json file as the FIRST argument in the comamnd line.
```console
   ./retail_for_all.sh /path/to/my_config.json
```
4. You can pass in overrides to the config file using the --key value when starting the container, ex:
```console
docker run -it --privileged --name r4all-test \
--rm -v ${R4ALL_DIR}:/usr/app/src --env \
PULSE_SERVER=unix:/tmp/pulseaudio.socket \
--env PULSE_COOKIE=/tmp/pulseaudio.cookie \
--volume /tmp/pulseaudio.socket:/tmp/pulseaudio.socket \
--volume /tmp/pulseaudio.client.conf:/etc/pulse/client.conf \
-p 8501:8501 \
-e DISPLAY=$DISPLAY  --user $(id -u) -w /usr/app/src \
--group-add=audio --device /dev/snd r4all:0.0.1 \
--nogpt
```
5. open your browser to localhost:8501 to see the GUI interface

Values in the config file can be overriden by passing option commandline arguments (see sample output below)

## Notice for FFmpeg

FFmpeg is an open source project licensed under the LGPL or GPL (depending on configuration). See [FFmpeg Legal Information](https://www.ffmpeg.org/legal.html). You are solely responsible for determining if your use of FFmpeg requires any additional licenses. Intel is not responsible for obtaining any such licenses, nor liable for any licensing fees due, in connection with your use of FFmpeg.

# Known Issues

This is a sample workload for use in testing and performance analysis. It is not intended for production use. For current issues,
see the open issues tab.

# References

* [Introduction to Speech to Text AI](https://www.gladia.io/blog/introduction-to-speech-to-text-ai)
* [AI Translation at the edge](https://medium.com/the-click-reader/language-translation-using-hugging-face-and-python-in-3-lines-of-code-8f22374cf225)
