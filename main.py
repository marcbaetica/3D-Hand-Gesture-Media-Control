from assistant.assistant import Assistant
from pathlib import Path


"""
INSTANTIATE VIRTUAL ASSISTANT
"""
assistant = Assistant()


"""
PLAY AUDIO FILE
"""
audio_file = Path('audio_samples') / 'paint.wav'
assistant.play_audio_file(audio_file, initiate_time_series_graph=True)


"""
SHUT DOWN VIRTUAL ASSISTANT
"""
assistant.shut_down()
