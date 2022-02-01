import wave
from lib.path_processing import convert_relative_path_obj_or_string_to_absolute_path_string


def stream_wav_bytes_from_file(file):
    batch_size = 1024
    file = convert_relative_path_obj_or_string_to_absolute_path_string(file)
    wave_file_features = get_wav_file_features(file)
    frames_count = wave_file_features['total_frames']
    sample_width = wave_file_features['sample_width']
    with wave.open(file, 'rb') as wave_reader:
        for _ in range(int(frames_count/batch_size) + 1):
            yield wave_reader.readframes(batch_size)


def get_wav_file_features(file):
    """Takes path to a wav file and retrieves audio properties associated to that file.

    :param file: (str or pathlib.Path) Path of the wave file.
    :return: (dict) Dictionary containing wave file properties. Keys are: channels_count, compression_name,
                    compression_type, markers, number_of_frames, sampling_frequency_hz, sample_width
    """
    file = convert_relative_path_obj_or_string_to_absolute_path_string(file)
    with wave.open(file, 'rb') as wave_read:
        wave_properties = {
            'channels_count': wave_read.getnchannels(),
            'compression_name': wave_read.getcompname(),
            'compression_type': wave_read.getcomptype(),
            'markers': wave_read.getmarkers(),
            'total_frames': wave_read.getnframes(),
            'sampling_frequency_hz': wave_read.getframerate(),
            'sample_width': wave_read.getsampwidth()  # Bytes per frame.
        }
    return wave_properties
