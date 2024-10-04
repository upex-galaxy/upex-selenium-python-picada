import json
import os
from tests.root import get_root


def save_json_to_file(json_data: object, dir_path: str, file_name: str):
    tests_dir = get_root()
    # This is the path to the data directory
    data_dir = os.path.join(tests_dir, dir_path)
    # Create the data directory if it does not exist
    os.makedirs(data_dir, exist_ok=True)
    # Save JSON data to a file
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=4)