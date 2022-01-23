import os
import sys
from dotenv import load_dotenv
from pyaudio import PyAudio
from time import perf_counter
from threading import Thread


load_dotenv()

try:
    SAMPLE_FREQUENCY = int(os.environ['SAMPLE_FREQUENCY'])
    BIT_DEPTH = int(os.environ['BIT_DEPTH'])
    AUDIO_CHANNELS = int(os.environ['AUDIO_CHANNELS'])
except KeyError as e:
    print(f'ERROR: Could not load environment variable [{e}]. Please check the .env file definitions.')
    sys.exit(1)
except ValueError as e:
    print(f'ERROR: {e}. Please check the .env file definitions for appropriate values.')
    sys.exit(1)


class DigitalAssistant:
    def __init__(self, name):
        print(f'Loading digital assistant: {name}')
        self.name = name
        self.port_audio = PyAudio()
        self.microphone_frames = []
        self.listening_stream = self.open_listening_stream_on_port_audio()
        self.capture_stream_data()  # TODO: thread it.
        self.response_stream = None

    def open_listening_stream_on_port_audio(self):
        return self.port_audio.open(
                                    rate=SAMPLE_FREQUENCY,
                                    channels=AUDIO_CHANNELS,
                                    format=self.port_audio.get_format_from_width(int(BIT_DEPTH/8)),
                                    input=True,
                                    frames_per_buffer=1024  # wha?
                                )

    def capture_stream_data(self):
        print(perf_counter())
        for _ in range(41):
            print(f'Before reading frames: {len(self.microphone_frames)}')
            frames = self.listening_stream.read(int(SAMPLE_FREQUENCY/4))
            self.microphone_frames += [int(item, base=16) for item in frames.hex('-', bytes_per_sep=2).split('-')]
            print(f'After reading frames: {len(self.microphone_frames)}')
            if len(self.microphone_frames) > int(SAMPLE_FREQUENCY*3):
                self.microphone_frames = self.microphone_frames[int(SAMPLE_FREQUENCY/4):]
            print(f'After cleaning frames: {len(self.microphone_frames)}')
        print(perf_counter())
