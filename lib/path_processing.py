from pathlib import Path


def convert_to_string_if_path_obj(obj):
    if isinstance(obj, str):
        return str(Path(obj).absolute())
    elif isinstance(obj, Path):
        return str(obj.absolute())
    else:
        raise TypeError(f'Expected {obj} to be of type String or pathlib.Path. Instead found type {type(obj)}.')
