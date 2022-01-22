import os
import sys
from lib.assistant import choose_random_assistant_from_file
from digital_assistant import DigitalAssistant
from dotenv import load_dotenv


load_dotenv()

try:
    SAMPLE_FREQUENCY = os.environ['SAMPLE_FREQUENCY']
    BIT_DEPTH = os.environ['BIT_DEPTH']
    AUDIO_CHANNELS = os.environ['AUDIO_CHANNELS']
except KeyError as e:
    print(f'ERROR: Could not load environment variable [{e}]. Please check the .env file definitions.')
    sys.exit(1)


assistant = choose_random_assistant_from_file('assistants.json')
digital_assistant = DigitalAssistant(assistant)
