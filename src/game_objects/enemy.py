import os
from random import randint

import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, path: list) -> None:
        super().__init__()

        curdir = os.path.dirname(__file__)
        image_path = os.path.join(curdir, "..", "assets", "enemy.png")
        hit_image_path = os.path.join(curdir, "..", "assets", "enemy_hit.png")
        dying_image_path = os.path.join(
            curdir, "..", "assets", "enemy_dying.png")

        self.normal_image: pygame.Surface = pygame.image.load(image_path)
        self.hit_image: pygame.Surface = pygame.image.load(hit_image_path)
        self.dying_image: pygame.Surface = pygame.image.load(dying_image_path)

        self.normal_image = self.normal_image.convert()
        self.hit_image = self.hit_image.convert()
        self.dying_image = self.dying_image.convert()

        self.image = self.normal_image
        self.rect = self.image.get_rect()

        self.path = path
        self.pos_on_path = 0
        self._update_pos()

        self.timer = 0

        self.health = 100
        self.hit_timer = 0

        self.dying = False
        self.dying_timer = 10

    def hit(self, tower_pos: tuple, tower_range: int):
        tower_x, tower_y = tower_pos
        return self.x in range(tower_x - tower_range, tower_x + tower_range + 1) and self.y in range(tower_y - tower_range, tower_y + tower_range + 1)

    def update(self, damage: int = None):
        if damage is not None:
            self.health -= damage
            self.image = self.hit_image
            self.hit_timer = 7
            if self.health <= 0:
                self.dying = True

        elif self.hit_timer > 0:
            self.hit_timer -= 1
            if self.hit_timer == 0:
                self.image = self.normal_image

        elif self.pos_on_path < len(self.path) - 1:
            self.timer += 1
            if self.timer >= 90:
                self.timer = 0
                self.pos_on_path += 1
                self._update_pos()

        if self.dying:
            self.image = self.dying_image
            self.dying_timer -= 1
            if self.dying_timer == 0:
                self.kill()

    def _update_pos(self):
        self.x = self.path[self.pos_on_path][0]
        self.y = self.path[self.pos_on_path][1]

        self.rect.x = self.x*20 + randint(2, 8)
        self.rect.y = self.y*20 + randint(2, 8)
