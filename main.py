from lib.assistant import choose_random_assistant_from_file
from lib.audio_processing import read_wave_file
from digital_assistant import DigitalAssistant
from pathlib import Path


# assistant = choose_random_assistant_from_file('assistants.json')
# digital_assistant = DigitalAssistant(assistant)



audio_samples_folder = Path('audio_samples')
read_wave_file(audio_samples_folder / 'paint.wav')
# print(audio_samples_folder)
