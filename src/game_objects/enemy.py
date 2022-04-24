import os
from random import randint

import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, path: list) -> None:
        super().__init__()

        self.status = {}
        self.status["move_timer"] = 1
        self.status["health"] = 100
        self.status["hit_timer"] = 0
        self.status["dying"] = False
        self.status["dying_timer"] = 10

        self.images = {}
        self.image = None
        self.__load_images()

        self.rect = self.image.get_rect()

        self.path = path
        self.pos_on_path = 0
        self._update_pos()

    @property
    def dying(self) -> bool:
        return self.status["dying"]

    def hit(self, tower_pos: tuple, tower_range: int) -> bool:
        tower_x, tower_y = tower_pos
        if self.x in range(tower_x - tower_range, tower_x + tower_range + 1):
            if self.y in range(tower_y - tower_range, tower_y + tower_range + 1):
                return True
        return False

    def update(self, damage: int = None) -> None:
        self._take_damage(damage)
        self._update_timers()
        self._move()
        self._update_image()
        if self.status["dying"]:
            self.image = self.images["dying"]
            self.status["dying_timer"] -= 1
            if self.status["dying_timer"] == 0:
                self.kill()

    def _update_timers(self) -> None:
        if self.status["dying"] and self.status["dying_timer"] > 0:
            self.status["dying_timer"] -= 1

        elif self.pos_on_path < len(self.path) - 1:
            self.status["move_timer"] += 1
            if self.status["move_timer"] >= 60:
                self.status["move_timer"] = 0

        if self.status["hit_timer"] > 0:
            self.status["hit_timer"] -= 1
        else:
            self._update_image()

    def _update_image(self) -> None:
        if self.status["dying"]:
            self.image = self.images["dying"]
        elif self.status["hit_timer"] > 0:
            self.image = self.images["hit"]
        else:
            self.image = self.images["normal"]

    def _take_damage(self, damage: int) -> None:
        if damage is not None:
            self.status["health"] -= damage
            self.status["hit_timer"] = 7
            if self.status["health"] <= 0:
                self.status["dying"] = True
            self._update_image()

    def _move(self) -> None:
        if not self.status["dying"] and self.status["move_timer"] == 0:
            self.pos_on_path += 1
            self._update_pos()

    def _update_pos(self) -> None:
        self.x = self.path[self.pos_on_path][0]
        self.y = self.path[self.pos_on_path][1]

        self.rect.x = self.x*20 + randint(2, 8)
        self.rect.y = self.y*20 + randint(2, 8)

    def __load_images(self):
        curdir = os.path.dirname(__file__)
        image_path = os.path.join(curdir, "..", "assets", "enemy.png")
        hit_image_path = os.path.join(curdir, "..", "assets", "enemy_hit.png")
        dying_image_path = os.path.join(
            curdir, "..", "assets", "enemy_dying.png")

        self.images["normal"] = pygame.image.load(image_path).convert()
        self.images["hit"] = pygame.image.load(hit_image_path).convert()
        self.images["dying"] = pygame.image.load(dying_image_path).convert()

        self._update_image()
