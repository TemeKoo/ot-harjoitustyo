import pygame
from helpers.level_loader import LevelLoader

from game_objects.tiles import BaseTile, BuildableTile, PathTile


class Field():
    def __init__(self, level: int, loader: LevelLoader):
        self.level = level
        self.loader = loader
        self.side_length = 20

        self._generate_field()

    def _generate_field(self):
        field_data = self.loader.get_field(self.level)

        if field_data:
            self.width = len(field_data[0])*self.side_length
            self.height = len(field_data)*self.side_length

            self.rect = pygame.Rect(0, 0, self.width, self.height)

            self.tiles = pygame.sprite.Group()

            for row, _ in enumerate(field_data):
                for column in range(len(field_data[row])):
                    new_tile = None
                    new_x = column
                    new_y = row
                    tile_number = field_data[row][column]
                    if tile_number == 0:
                        new_tile = BuildableTile(new_x, new_y, new_x*self.side_length, new_y*self.side_length)
                    elif tile_number == 1:
                        new_tile = PathTile(new_x, new_y, new_x*self.side_length, new_y*self.side_length)
                    elif tile_number == 2:
                        new_tile = BaseTile(new_x, new_y, new_x*self.side_length, new_y*self.side_length)
                        self.base_tile = new_tile
                    new_tile.scale(self.side_length)
                    self.tiles.add(new_tile)

    def update(self, base_damage: int = None) -> None:
        self.tiles.update(damage = base_damage)

    def scale(self, side_length: int) -> None:
        self.side_length = side_length
        self._generate_field()

    def get_tiles(self) -> pygame.sprite.Group:
        """Returns the tiles of the field."""
        return self.tiles
    
    def get_base_tile(self) -> BaseTile:
        """Returns the base tile of the field."""
        return self.base_tile

    def get_image_size(self) -> tuple:
        """Returns the size of the field in a tuple in the form of (width, height)."""
        return (self.width, self.height)
