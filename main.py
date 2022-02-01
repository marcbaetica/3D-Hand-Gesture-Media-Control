# from audio_processing.audio_utils import read_wave_file
# from pathlib import Path
#
#
# # assistant = choose_random_assistant_from_file('assistants.json')
# # digital_assistant = DigitalAssistant(assistant)
#
#
#
# audio_samples_folder = Path('audio_samples')
# read_wave_file(audio_samples_folder / 'paint.wav')
# # print(audio_samples_folder)


from audio_processing.audio_utils import play_audio_file
from pathlib import Path
from pprintpp import pprint


audio_file = Path('audio_samples') / 'paint.wav'
print(audio_file)


play_audio_file(audio_file)
