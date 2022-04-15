import os

import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, path: list) -> None:
        super().__init__()

        curdir = os.path.dirname(__file__)
        image_path = os.path.join(curdir, "..", "assets", "enemy.png")
        self.image: pygame.Surface = pygame.image.load(image_path)

        self.image = self.image.convert()

        self.rect = self.image.get_rect()

        self.path = path
        self.pos_on_path = 0
        self._update_pos()

    def update(self):
        if self.pos_on_path < len(self.path) - 1:
            self.pos_on_path += 1
            self._update_pos()
    
    def _update_pos(self):
        self.x = self.path[self.pos_on_path][0]
        self.y = self.path[self.pos_on_path][1]

        self.rect.x = self.x*20 + 5
        self.rect.y = self.y*20 + 5
