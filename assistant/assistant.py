import json
import pyaudio
from audio_processing.audio_processing_utils import AudioProcessingUtils
from random import choice


ASSISTANTS_FILE = 'assistant/assistants.json'


class Assistant:
    def __init__(self, assistant_choice=None):
        self.assistant = assistant_choice if assistant_choice else self.choose_random_assistant_from_file(ASSISTANTS_FILE)
        self.port_audio = self._start_port_audio()

    @staticmethod
    def choose_random_assistant_from_file(file):
        """Returns name of a digital assistant chosen at random from an assistants file.

        :param file: (str) Name of the file containing the assistants.
        :return: (str) Name of the assistant.
        """
        with open(file, 'r') as f:
            assistant = choice(json.load(f)['assistants'])
            print(f'Loaded assistant {assistant["name"]}.')
            return assistant

    def play_audio_file(self, file_path):
        AudioProcessingUtils.play_audio_file(file_path, self.port_audio)

    @staticmethod
    def _start_port_audio():
        return pyaudio.PyAudio()

    def shut_down(self):
        print(f'{self.assistant["name"]}: Shutting down...')
        self.port_audio.terminate()  # Shuts down port audio instance and all associated streams.
