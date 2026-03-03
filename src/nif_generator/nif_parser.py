import struct

class NifParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_file(self):
        with open(self.file_path, 'rb') as f:
            self.data = f.read()

    def parse(self):
        # Example of parsing logic (this should be customized based on NIF file structure)
        header_format = '4sI'
        header_size = struct.calcsize(header_format)
        header_data = self.data[:header_size]

        header = struct.unpack(header_format, header_data)
        return {'magic': header[0].decode('utf-8'), 'version': header[1]}

# Example usage
if __name__ == '__main__':
    parser = NifParser('path/to/nif_file.nif')
    parser.read_file()
    info = parser.parse()
    print(info)