from lib.assistant import choose_random_assistant_from_file
from digital_assistant import DigitalAssistant


assistant = choose_random_assistant_from_file('assistants.json')
digital_assistant = DigitalAssistant(assistant)
