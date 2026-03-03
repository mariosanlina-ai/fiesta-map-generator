import os
import json


def read_json(file_path):
    """Reads a JSON file and returns the data."""
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    """Writes data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def read_text_file(file_path):
    """Reads a text file and returns its content."""
    with open(file_path, 'r') as file:
        return file.read()


def write_text_file(file_path, content):
    """Writes content to a text file."""
    with open(file_path, 'w') as file:
        file.write(content)
