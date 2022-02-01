import unittest
from lib.path_processing import convert_relative_path_obj_or_string_to_absolute_path_string
from pathlib import Path


class TestPathProcessing(unittest.TestCase):
    def test_path_object_converted_to_string(self):
        some_path = Path('some_folder/some_file.wav')
        self.assertTrue(isinstance(convert_relative_path_obj_or_string_to_absolute_path_string(some_path), str))

    def test_path_string_remains_string(self):
        some_path = 'some_folder/some_file.wav'
        self.assertTrue(isinstance(convert_relative_path_obj_or_string_to_absolute_path_string(some_path), str))

    def test_path_string_conversion_outputs_absolute_path(self):
        some_path_string = 'some_folder'
        self.assertTrue(Path.is_absolute(Path(convert_relative_path_obj_or_string_to_absolute_path_string(some_path_string))))
        some_path_obj = Path('some_folder')
        self.assertTrue(Path.is_absolute(Path(convert_relative_path_obj_or_string_to_absolute_path_string(some_path_obj))))

    def test_path_string_to_string_raises_type_error(self):
        some_wrong_paths = [0, 1.5, [], {}, (1)]
        for wrong_path_obj in some_wrong_paths:
            with self.assertRaises(TypeError):
                convert_relative_path_obj_or_string_to_absolute_path_string(wrong_path_obj)


if __name__ == '__main__':
    unittest.main()
