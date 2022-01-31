import wave
from lib.path_processing import convert_to_string_if_path_obj


def stream_wav_bytes_from_file(file):
    data = []
    return data


def get_wav_file_attributes(file):
    file = convert_to_string_if_path_obj(file)
    with wave.open(file, 'r') as wave_read:
        print(wave_read.getnchannels())
        print(wave_read.getsampwidth())
        print(wave_read.getframerate())
        print(wave_read.getnframes())
        print(wave_read.getcomptype())
        print(wave_read.getcompname())
        print(wave_read.getmarkers())
