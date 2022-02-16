import pyaudio
import wave
from audio_processing.file_processing.audio_file_processing_factory import AudioFileProcessingFactory
from graphical_renderings.time_series_graph import run_flask_server
from threading import Thread


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


# TODO: everything above this should be refactored and cleaned up!

class AudioProcessingUtils:
    @staticmethod
    def play_audio_file(file, port_audio, initiate_time_series_graph=False):  # TODO: Break down to return frames in individual function.
        audio_stream = AudioFileProcessingFactory.get_audio_byte_stream_from_file(file)
        audio_features = AudioFileProcessingFactory.get_audio_file_features(file)
        stream = port_audio.open(rate=audio_features['sampling_frequency_hz'],
                                 channels=audio_features['channels_count'],
                                 format=port_audio.get_format_from_width(audio_features['sample_width']),
                                 output=True,
                                 # TODO: Centralize 1024. 1024 frames are indeed retrieved (2 bytes per frame).
                                 frames_per_buffer=1024*audio_features['sample_width'])
        if initiate_time_series_graph:
            thread = Thread(target=run_flask_server)
            thread.start()
        # Processing batches of audio frames.
        next_batch = next(audio_stream, None)  # b''
        while next_batch is not None:
            # print(AudioProcessingUtils._convert_audio_byte_frames_to_int(next_batch, 2))
            stream.write(next_batch)
            next_batch = next(audio_stream, None)

    @staticmethod
    def _convert_audio_byte_frames_to_int(frames, bytes_per_frame):
        return [int(hex_value, base=16) for hex_value in frames.hex('-', bytes_per_sep=bytes_per_frame).split('-')]

    def _open_time_series_plot(self):
        pass

    def _update_time_series_plot(self, new_data):
        pass
