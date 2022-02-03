import pyaudio
import wave
from audio_processing.audio_processing_factory import AudioFileProcessingFactory
from audio_processing.wav_audio_processing import get_wav_file_features  # TODO: factory for this as well!


def record_audio(sample_frequency, bit_rate, audio_channels):
    port_audio = pyaudio.PyAudio()

    stream = port_audio.open(rate=sample_frequency,
                             channels=audio_channels,
                             format=pyaudio.paInt16,
                             input=True,
                             frames_per_buffer=1024)
    print('Recording!')

    frames = []

    for i in range(int(44100/1024*2)):
        frames.append(stream.read(1024))

    print('Done recording!')
    port_audio.terminate()


def save_recording(frames, port_audio, sample_frequency, bit_rate, audio_channels):
    with wave.open('recording_16bit.wav', 'wb') as wave_writer:
        wave_writer.setsampwidth(port_audio.get_sample_size(pyaudio.paInt16))
        wave_writer.setframerate(sample_frequency)
        wave_writer.setnchannels(audio_channels)
        wave_writer.writeframes(b''.join(frames))


def convert_microphone_byte_frames_to_int(frames):
    return [int(item, base=16) for item in frames.hex('-', bytes_per_sep=2).split('-')]


# TODO: everything above this should be refactored and cleaned up!

def play_audio_file(file):
    audio_stream = AudioFileProcessingFactory.get_audio_byte_stream_from_file(file)
    audio_features = AudioFileProcessingFactory.get_audio_file_features(file)
    port_audio = pyaudio.PyAudio()
    stream = port_audio.open(rate=audio_features['sampling_frequency_hz'],
                             channels=audio_features['channels_count'],
                             format=port_audio.get_format_from_width(int(16 / 8)),  # TODO: Investigate if 'sample_width'!
                             output=True,
                             # TODO: Should be double because of 'sample_width' of 2 so each next() generates 2048 bytes of data.
                             # TODO: Centralize data since I can't extract data from generator function.
                             frames_per_buffer=1024)
    next_batch = next(audio_stream, None)  # b''
    while next_batch is not None:
        stream.write(next_batch)
        next_batch = next(audio_stream, None)
    port_audio.terminate()
