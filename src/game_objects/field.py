import pygame
from helpers.level_loader import LevelLoader
from game_objects.tiles import BuildableTile, PathTile ,BaseTile


class Field():
    def __init__(self, level: int, loader: LevelLoader):
        self.level = level
        self.loader = loader

        field_data = loader.get_field(self.level)

        if field_data:
            self.width = len(field_data[0])*20
            self.height = len(field_data)*20

            self.rect = pygame.Rect(0, 0, self.width, self.height)

            self.tiles = pygame.sprite.Group()

            for row in range(len(field_data)):
                for column in range(len(field_data[row])):
                    new_tile = None
                    new_x = column*20
                    new_y = row*20
                    tile_number = field_data[row][column]
                    if tile_number == 0:
                        new_tile = BuildableTile(new_x, new_y)
                    elif tile_number == 1:
                        new_tile = PathTile(new_x, new_y)
                    elif tile_number == 2:
                        new_tile = BaseTile(new_x, new_y)
                    self.tiles.add(new_tile)

    def get_tiles(self) -> pygame.sprite.Group:
        """Returns the tiles of the field."""
        return self.tiles

    def get_size(self) -> tuple:
        """Returns the size of the field in a tuple in the form of (width, height)."""
        return (self.width, self.height)
