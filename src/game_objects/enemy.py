import os
from random import randint

import pygame

BASE_DAMAGED = 2
ENEMY_DAMAGE = 10
ENEMY_MOVE_COOLDOWN = 60


class Enemy(pygame.sprite.Sprite):
    """Represents a simple enemy."""

    def __init__(self, path: list) -> None:
        super().__init__()

        self.status = {}
        self.status["move_timer"] = 1
        self.status["health"] = 100
        self.status["hit_timer"] = 0
        self.status["dying"] = False
        self.status["dying_timer"] = 10
        self.status["in_base"] = False

        self.images = {}
        self.image = None
        self.__load_images()

        self.rect = self.image.get_rect()

        self.path = path
        self.pos_on_path = 0
        self.__update_pos()

    @property
    def dying(self) -> bool:
        """Returns if the enemy is currently dying.

        Returns:
            dying (bool): True if enemy is dying, False if not.
        """
        return self.status["dying"]

    def hit(self, tower_pos: tuple, tower_range: int) -> bool:
        """Returns if the enemy got hit by the tower.

        Args:
          tower_pos (tuple): Position of tower on the field in tuple (x, y).
          tower_range (int): Range of the tower.

        Returns:
            hit (bool): True if enemy got hit, False if not.
        """
        tower_x, tower_y = tower_pos
        if self.x in range(tower_x - tower_range, tower_x + tower_range + 1):
            if self.y in range(tower_y - tower_range, tower_y + tower_range + 1):
                return True
        return False

    def update(self, damage: int = None) -> None:
        """Override of the pygame update function.
        Use without arguments to update cooldowns once per frame.

        Args:
          damage (int): The enemy takes this amount of damage. (Default value = None)
        """

        if damage is not None:
            self.__take_damage(damage)
        else:
            self.__update_timers()
            self.__update_status()

        self.__update_image()

    def __update_timers(self) -> None:
        if self.status["dying"] and self.status["dying_timer"] > 0:
            self.status["dying_timer"] -= 1

        else:
            self.status["move_timer"] += 1
            if self.status["move_timer"] >= ENEMY_MOVE_COOLDOWN:
                self.status["move_timer"] = 0

        if self.status["hit_timer"] > 0:
            self.status["hit_timer"] -= 1

    def __update_status(self) -> None:
        if self.status["dying_timer"] == 0:
            self.kill()

        if not self.status["dying"]:
            if self.status["health"] <= 0:
                self.status["dying"] = True
                return

            if self.status["move_timer"] == 0:
                self.__move()

            if self.status["in_base"]:
                self.__damage_base()

    def __take_damage(self, damage: int) -> None:
        self.status["health"] -= damage
        self.status["hit_timer"] = 7

    def __move(self) -> None:
        if self.pos_on_path < len(self.path) - 1:
            self.pos_on_path += 1
            self.__update_pos()

        if self.pos_on_path == len(self.path) - 1:
            self.status["in_base"] = True

    def __damage_base(self) -> None:
        pygame.event.post(pygame.event.Event(
            pygame.USEREVENT, custom_type=BASE_DAMAGED, damage=ENEMY_DAMAGE))
        self.kill()

    def __update_pos(self) -> None:
        self.x = self.path[self.pos_on_path][0]
        self.y = self.path[self.pos_on_path][1]

        self.rect.x = self.x*20 + randint(2, 8)
        self.rect.y = self.y*20 + randint(2, 8)

    def __update_image(self) -> None:
        if self.status["dying"]:
            self.image = self.images["dying"]
        elif self.status["hit_timer"] > 0:
            self.image = self.images["hit"]
        else:
            self.image = self.images["normal"]

    def __load_images(self) -> None:
        curdir = os.path.dirname(__file__)
        image_path = os.path.join(curdir, "..", "assets", "enemy.png")
        hit_image_path = os.path.join(curdir, "..", "assets", "enemy_hit.png")
        dying_image_path = os.path.join(
            curdir, "..", "assets", "enemy_dying.png")

        self.images["normal"] = pygame.image.load(image_path).convert()
        self.images["hit"] = pygame.image.load(hit_image_path).convert()
        self.images["dying"] = pygame.image.load(dying_image_path).convert()

        self.__update_image()
