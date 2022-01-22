import os
import sys
from dotenv import load_dotenv
from pyaudio import PyAudio
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
        self.listening_stream = Thread(target=self.open_listening_stream_on_port_audio())
        self.response_stream = None

    def open_listening_stream_on_port_audio(self):
        listening_stream = self.port_audio.open(
                                    rate=SAMPLE_FREQUENCY,
                                    channels=AUDIO_CHANNELS,
                                    format=self.port_audio.get_format_from_width(int(BIT_DEPTH/8)),
                                    input=True,
                                    frames_per_buffer=1024
                                )
        for _ in range(20):
            frame = listening_stream.read(1024)
            # print(frame, len(frame))
            # print(type(frame))
            print([int(item, base=16) for item in frame.hex('-', bytes_per_sep=2).split('-')])
