from audio_processing.audio_processing_utils import AudioProcessingUtils
from pathlib import Path


audio_file = Path('audio_samples') / 'paint.wav'
print(audio_file)

AudioProcessingUtils.play_audio_file(audio_file)
