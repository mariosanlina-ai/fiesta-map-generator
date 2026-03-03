import random

class MapGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for _ in range(width)] for _ in range(height)]

    def generate_random_map(self):
        for y in range(self.height):
            for x in range(self.width):
                self.map[y][x] = random.choice([0, 1])  # 0 represents empty, 1 represents filled

    def display_map(self):
        for row in self.map:
            print(' '.join(str(cell) for cell in row))


# Example usage:
if __name__ == '__main__':
    generator = MapGenerator(10, 10)
    generator.generate_random_map()
    generator.display_map()