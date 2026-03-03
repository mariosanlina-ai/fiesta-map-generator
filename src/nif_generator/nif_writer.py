# NIF Writer

"""
This module provides functions to write and generate NIF (Ninja Information Files).
"""

import struct


def write_nif_file(file_path, data):
    """
    Writes data to a NIF file.
    
    :param file_path: Path to the NIF file to be created.
    :param data: Dictionary containing the data to write to the NIF file.
    """
    with open(file_path, 'wb') as nif_file:
        # Example structure, update according to actual NIF specification.
        nif_file.write(struct.pack('<I', len(data)))  # Example header
        for key, value in data.items():
            nif_file.write(struct.pack('<I', key))  # Example data
            nif_file.write(struct.pack('<f', value))  # Example data


if __name__ == '__main__':
    sample_data = {1: 12.34, 2: 56.78}
    write_nif_file('sample.nif', sample_data)