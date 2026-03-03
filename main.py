import click

class MapGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate_map(self):
        # Simple map generation logic
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

@click.command()  
@click.option('--width', default=10, help='Width of the map.')
@click.option('--height', default=10, help='Height of the map.')
def main(width, height):
    """Generates a map based on specified width and height."
    try:
        generator = MapGenerator(width, height)
        generated_map = generator.generate_map()
        click.echo('Generated Map:')
        for row in generated_map:
            click.echo(row)
    except Exception as e:
        click.echo(f'Error generating map: {str(e)}')

if __name__ == '__main__':
    main()