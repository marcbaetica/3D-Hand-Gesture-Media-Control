import os
from pathlib import Path
from pprintpp import pprint
from zipfile import ZipFile


def get_list_of_all_files_at(relative_path):
    all_files = []
    for path, directories, files in os.walk(relative_path):
        for file in files:
            all_files.append(str(Path.resolve(Path(path).absolute() / file)))
    return all_files


def discard_any_unwanted_items(original_list, items_to_ignore):
    return [item for item in original_list if not any([item_to_ignore in item for item_to_ignore in items_to_ignore])]


def zip_files(file_paths, archive_name):
    with ZipFile(f'results/{archive_name}', 'w') as zip_file:
        for file in file_paths:
            zip_file.write(file, file.split('results')[1])


def generate_zip_of_results():
    items_to_ignore = ['.gitignore', '.idea', '.git']
    print(f'Generating zip archive of results. All items containing {items_to_ignore} will be discarded.')
    all_files = get_list_of_all_files_at('..')
    all_files = discard_any_unwanted_items(all_files, items_to_ignore)
    print('Files that will be archived:')
    pprint(all_files)
    zip_files(all_files, 'result_123.zip')  # TODO: change name
