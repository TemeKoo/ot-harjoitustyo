import pygame
import os
from helpers.level_loader import LevelLoader


class Field(pygame.sprite.Sprite):
    def __init__(self, level: int, loader: LevelLoader):
        super().__init__()
        
        self.level = level
        self.loader = loader

        field_data = loader.get_field(self.level)

        if field_data:
            width = len(field_data[0])*20
            height = len(field_data)*20
            self.image = pygame.Surface((width, height))

            curdir = os.path.dirname(__file__)
            texture_path = os.path.join(curdir, "..", "assets", "tiles")

            buildable_tile = pygame.image.load(os.path.join(texture_path, "buildable.png"))
            path_tile = pygame.image.load(os.path.join(texture_path, "path.png"))
            base_tile = pygame.image.load(os.path.join(texture_path, "base.png"))

            textures = {
                0: buildable_tile,
                1: path_tile,
                2: base_tile
            }

            for row in range(len(field_data)):
                for column in range(len(field_data[row])):
                    self.image.blit(textures[field_data[row][column]], (column*20, row*20))

            self.image = self.image.convert()
            self.rect = self.image.get_rect()
    
    def get_size(self) -> tuple:
        """Returns the size of the field in a tuple in the form of (width, height)."""
        return (self.image.get_width(), self.image.get_height())