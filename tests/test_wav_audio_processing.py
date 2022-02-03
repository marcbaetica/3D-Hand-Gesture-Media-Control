import unittest
from audio_processing.file_processing.wav_audio_processing import get_wav_file_features
from pathlib import Path


class TestWavAudioProcessing(unittest.TestCase):
    def test_correct_wav_file_features_extraction(self):
        sample_wav_file = Path('tests/audio_samples/paint.wav')
        expected_audio_file_features = {
            'channels_count': 1,
            'compression_name': 'not compressed',
            'compression_type': 'NONE',
            'markers': None,
            'total_frames': 290304,
            'sampling_frequency_hz': 32000,
            'sample_width': 2
        }
        audio_file_features = get_wav_file_features(sample_wav_file)
        self.assertTrue(audio_file_features == expected_audio_file_features)


if __name__ == '__main__':
    unittest.main()
