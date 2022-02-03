from audio_processing.mp3_audio_processing import stream_mp3_bytes_from_file
from audio_processing.wav_audio_processing import stream_wav_bytes_from_file
from audio_processing.mp3_audio_processing import get_mp3_file_features
from audio_processing.wav_audio_processing import get_wav_file_features
from lib.path_processing import convert_relative_path_obj_or_string_to_absolute_path_string


class AudioFileProcessingFactory:
    SUPPORTED_FORMATS = ['mp3', 'wav']  # DO NOT CHANGE ORDER!

    @classmethod
    def get_audio_byte_stream_from_file(cls, file):
        """TODO: Fill this in.

        :param file: (str or pathlib.Path) Path of the supported audio file.
        :return: (generator) Stream of audio file.
        """
        audio_format = cls.extract_audio_format_if_supported(file)
        if audio_format == cls.SUPPORTED_FORMATS[0]:
            return stream_mp3_bytes_from_file(file)
        elif audio_format == cls.SUPPORTED_FORMATS[1]:
            return stream_wav_bytes_from_file(file)

    @classmethod
    def get_audio_file_features(cls, file):
        audio_format = cls.extract_audio_format_if_supported(file)
        if audio_format == cls.SUPPORTED_FORMATS[0]:
            return stream_mp3_bytes_from_file(file)
        elif audio_format == cls.SUPPORTED_FORMATS[1]:
            return get_wav_file_features(file)

    @classmethod
    def extract_audio_format_if_supported(cls, file):
        audio_format = convert_relative_path_obj_or_string_to_absolute_path_string(file).split('.')[-1]
        if audio_format not in cls.SUPPORTED_FORMATS:
            raise ValueError(
                f'Audio file [{file}] is not in one of the supported formats. Supported formats: {cls.SUPPORTED_FORMATS}')
        return audio_format
