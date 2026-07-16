from contextlib import contextmanager
import json
import os
from pathlib import Path
import pulsectl
import pyaudio
import wave
import simpleaudio as sa
import sys
import time
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_directory_not_empty(directory_path):
    # Step 1: Check if the directory exists
    if not os.path.isdir(directory_path):
        return False
    # Step 2: Check if the directory is not empty
    if not os.listdir(directory_path):
        return False
    return True

def download_file(url, local_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(local_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
def create_local_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def download_directory(url, local_dir, logger=None):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href not in ('../', '/'):
            full_url = urljoin(url, href)
            parsed_url = urlparse(full_url)
            local_path = os.path.join(local_dir, parsed_url.path.lstrip('/'))

            if full_url.endswith('/'):
                # It's a directory, recurse into it
                create_local_directory(local_path)
                download_directory(full_url, local_path)
            else:
                # It's a file, download it
                create_local_directory(os.path.dirname(local_path))
                if logger is not None:
                    logger.debug(f"Downloading {full_url} to {local_path}")
                download_file(full_url, local_path)

def add_to_syspath(*paths):
    for path in paths:
        if isinstance(path, str):
            path = Path(path)
            abs_path = path.resolve()
            if str(abs_path) not in sys.path:
                sys.path.append(str(abs_path))

@contextmanager
def suppress_stdout():
    # Auxiliary function to suppress Whisper logs (it is quite verbose)
    # All credit goes to: https://thesmithfam.org/blog/2012/10/25/temporarily-suppress-console-output-in-python/
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


def get_sound_device(logger=None):
    sound_device = None
    do_not_use = ['spdif', 'samplerate', 'speexrate', 'upmix', 'vdownmix']
    with suppress_stdout():
        py_audio = pyaudio.PyAudio()
        for i in range(py_audio.get_device_count()):
            curr_sound_device = py_audio.get_device_info_by_index(i)
            curr_device_name = curr_sound_device.get('name')
            
            if logger:
                logger.debug(f"curr_sound_device = {curr_sound_device}")
            if curr_device_name in do_not_use:
                logger.debug(f"Invalid sound device {curr_device_name}, skipping")
                continue
            if curr_sound_device.get('maxInputChannels') > 0:
                sound_device = curr_sound_device
                # microphone is characterized by maxInputChannels > 0sound_device = curr_sound_device
                if sound_device:
                    # prefer pulse over all
                    if 'pulse' in curr_device_name.lower():
                        sound_device = curr_sound_device
                        break # no need to keep looking for other audio devices
        py_audio.terminate()
    return sound_device


def get_pactl_devices(logger=None):
    pulse = pulsectl.Pulse("get-devices")
    pactl_devices = pulse.source_list()
    pulse.close()
    return pactl_devices


def mute_audio_input_devices(mute=True, index=None, name=None, logger=None):
    pulse = pulsectl.Pulse("mute-unmute-devices")
    if index:
        if logger:
            logger.debug(f"muting({mute}) device with index {index}")
        pulse.source_mute(index, mute)
    elif name:
        source = pulse.get_source_by_name(name)
        if source:
            if logger:
                logger.debug(f"muting({mute}) device with name {name}")
            pulse.source_mute(source.index, mute)
    else:
        pactl_devices = get_pactl_devices()
        for pactl_device in pactl_devices:
            if logger:
                logger.debug(f"Muting({mute}) device with idex {pactl_device.index}")
            pulse.source_mute(pactl_device.index, mute)
    pulse.close()


def block_while_speaker_in_use(sleep_time=1, logger=None):
    with pulsectl.Pulse('wait-for-audio-playback-end') as pulse:
        while True:
            sink_inputs = pulse.sink_input_list()
            if not sink_inputs:
                if logger:
                    logger.debug("No audio playback detected, continuing program")
            else:
                if logger:
                    logger.debug("Audio playback in progress, blocking...")
            if logger:
                logger.debug(f"Sleeping for {sleep_time} seconds")
            time.sleep(sleep_time)


def play_wav(filename, wait_done=False):
    # Open the WAV file
    wav_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wav_obj.play()
    if wait_done:
        play_obj.wait_done()


