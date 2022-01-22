import os
import sys
from lib.audio_processing import record_audio
from dotenv import load_dotenv



load_dotenv()

try:
    SAMPLE_FREQUENCY = os.environ['SAMPLE_FREQUENCY']
    BIT_DEPTH = os.environ['BIT_DEPTH']
    AUDIO_CHANNELS = os.environ['AUDIO_CHANNELS']
except KeyError as e:
    print(f'ERROR: Could not load environment variable [{e}]. Please check the .env file definitions.')
    sys.exit(1)

record_audio(SAMPLE_FREQUENCY, BIT_DEPTH, AUDIO_CHANNELS)
