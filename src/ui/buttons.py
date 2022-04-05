import pygame
import os

from game_objects.tower import Tower


class GenericButton(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()

        self.x = x
        self.y = y

    def click(self):
        pass

    def action(self):
        pass


class TowerButton(GenericButton):
    def __init__(self, x, y):
        super().__init__(x, y)

        curdir = os.path.dirname(__file__)
        self.image: pygame.Surface = pygame.image.load(os.path.join(curdir, "..", "assets", "button.png"))

        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

    def click(self, pos) -> Tower:
        x, y = pos
        new_tower = Tower(x, y)
        return new_tower


class MenuButton(GenericButton):
    def __init__(self):
        super().__init__()