import pygame
from helpers.level_loader import LevelLoader

from game_objects.tiles import BaseTile, BuildableTile, PathTile


class Field():
    """Represents the playing field of the game."""

    def __init__(self, level: int, loader: LevelLoader):
        self.level = level
        self.loader = loader
        self.side_length = 20

        self.__generate_field()

    def __generate_field(self):
        field_data = self.loader.get_field(self.level)

        if field_data is None:
            return

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
                    new_tile = BuildableTile(
                        new_x, new_y, new_x*self.side_length, new_y*self.side_length)
                elif tile_number == 1:
                    new_tile = PathTile(
                        new_x, new_y, new_x*self.side_length, new_y*self.side_length)
                elif tile_number == 2:
                    new_tile = BaseTile(
                        new_x, new_y, new_x*self.side_length, new_y*self.side_length)
                    self.base_tile = new_tile
                new_tile.scale(self.side_length)
                self.tiles.add(new_tile)

    def update(self, base_damage: int = None) -> None:
        """Updates all the tiles of the field.
        Use without arguments once per frame to update cooldowns.

        Args:
            base_damage (int): The base takes this amount of damage. (Default value = None)
        """
        self.tiles.update(damage=base_damage)

    def scale(self, side_length: int) -> None:
        """Scales the field.

        Args:
            side_length (int): Wanted side length of one tile in pixels.
        """
        self.side_length = side_length
        self.__generate_field()

    def get_tiles(self) -> pygame.sprite.Group:
        """Returns all the tiles of the field.

        Returns:
            tiles (pygame.sprite.Group)

        """
        return self.tiles

    def get_base_tile(self) -> BaseTile:
        """Returns the base tile of the field.

        Returns:
            base_tile (game_objects.tiles.BaseTile)
        """
        return self.base_tile

    def get_image_size(self) -> tuple:
        """Returns the image size of the field.

        Returns:
            size (tuple): (width, height) in pixels.

        """
        return (self.width, self.height)
