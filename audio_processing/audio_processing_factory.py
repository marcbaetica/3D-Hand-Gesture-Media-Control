from audio_processing.mp3_audio_processing import get_mp3_byte_stream_from_file
from audio_processing.wav_audio_processing import get_wav_byte_stream_from_file


SUPPORTED_FORMATS = ['mp3', 'wav']  # DO NOT CHANGE ORDER!


def get_audio_byte_stream_from_file(file):
    """

    :param file:
    :return:
    """
    audio_format = file.split('.')[-1]
    if audio_format not in SUPPORTED_FORMATS:
        raise ValueError(f'Audio file [{file}] is not in one of the supported formats. Supported formats: {SUPPORTED_FORMATS}')
    if audio_format == SUPPORTED_FORMATS[0]:
        return get_mp3_byte_stream_from_file(file)
    elif audio_format == SUPPORTED_FORMATS[1]:
        return get_wav_byte_stream_from_file(file)
