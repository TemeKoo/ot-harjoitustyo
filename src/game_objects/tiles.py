import os

import pygame


class GenericTile(pygame.sprite.Sprite):
    def __init__(self, x, y, image_name: str):
        super().__init__()
        curdir = os.path.dirname(__file__)
        image_path = os.path.join(curdir, "..", "assets", "tiles", image_name)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PathTile(GenericTile):
    def __init__(self, x, y):
        image_name = "path.png"
        super().__init__(x, y, image_name=image_name)


class BuildableTile(GenericTile):
    def __init__(self, x, y):
        image_name = "buildable.png"
        super().__init__(x, y, image_name=image_name)


class BaseTile(GenericTile):
    def __init__(self, x, y):
        image_name = "base.png"
        super().__init__(x, y, image_name=image_name)
