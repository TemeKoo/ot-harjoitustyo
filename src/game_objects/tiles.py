import os

import pygame


class GenericTile(pygame.sprite.Sprite):
    def __init__(self, x, y, img_x, img_y, image_name: str):
        super().__init__()
        
        self.x = x
        self.y = y
        
        curdir = os.path.dirname(__file__)
        image_path = os.path.join(curdir, "..", "assets", "tiles", image_name)
        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()
        self.rect.x = img_x
        self.rect.y = img_y
    
    def get_pos(self) -> tuple:
        """Returns the field position of the tile"""
        return (self.x, self.y)

    def get_img_pos(self) -> tuple:
        """Returns the surface position of the tile."""
        return (self.rect.x, self.rect.y)


class PathTile(GenericTile):
    def __init__(self, x, y, img_x, img_y):
        image_name = "path.png"
        super().__init__(x, y, img_x, img_y, image_name=image_name)


class BuildableTile(GenericTile):
    def __init__(self, x, y, img_x, img_y):
        image_name = "buildable.png"
        super().__init__(x, y, img_x, img_y, image_name=image_name)


class BaseTile(GenericTile):
    def __init__(self, x, y, img_x, img_y):
        image_name = "base.png"
        super().__init__(x, y, img_x, img_y, image_name=image_name)
