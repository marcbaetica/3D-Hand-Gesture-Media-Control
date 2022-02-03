from audio_processing.audio_utils import play_audio_file
from pathlib import Path


audio_file = Path('audio_samples') / 'paint.wav'
print(audio_file)

play_audio_file(audio_file)
