import os

import pygame


class GenericSprite(pygame.sprite.Sprite):
    """A generic sprite class to extend to different game objects."""

    def __init__(self):
        super().__init__()

        self.status = {}

        self.images = {}
        self.image = None

    def load_images(self, image_data: dict) -> None:
        """Loads images of the sprite from a dictionary of names.
        Meant to be used in the __init__ method of child.

        Args:
            image_data (dict): A dictionary containing name, image_name pairs,
            where image_name is an iterable containing the path inside assets folder.
        """
        curdir = os.path.dirname(__file__)

        for name, image_name in image_data.items():
            image_path = os.path.join(curdir, "..", "assets", *image_name)

            self.images[name] = pygame.image.load(image_path).convert()
