from pathlib import Path


def convert_relative_path_obj_or_string_to_absolute_path_string(obj):
    if isinstance(obj, str):
        return str(Path(obj).absolute())
    elif isinstance(obj, Path):
        return str(obj.absolute())
    else:
        raise TypeError(f'Expected {obj} to be of type String or pathlib.Path. Instead found type {type(obj)}.')
