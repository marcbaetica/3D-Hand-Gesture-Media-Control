import json
from random import choice


def choose_random_assistant_from_file(file):
    """Returns name of a digital assistant chosen at random from an assistants file.

    :param file: (str) Name of the file containing the assistants.
    :return: (str) Name of the assistant.
    """
    with open(file, 'r') as f:
        assistant = choice(json.load(f)['assistants'])
        return assistant['name']
