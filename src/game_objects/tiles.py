import os

import pygame

GAME_OVER = 3
BASE_HIT_TIMER = 12

class GenericTile(pygame.sprite.Sprite):
    def __init__(self, x, y, img_x, img_y, image_name: str = None):
        super().__init__()

        self.x = x
        self.y = y

        if image_name is not None:
            curdir = os.path.dirname(__file__)
            image_path = os.path.join(curdir, "..", "assets", "tiles", image_name)
            self.image = pygame.image.load(image_path)

            self.rect = self.image.get_rect()
            self.rect.x = img_x
            self.rect.y = img_y

    def scale(self, side_length: int) -> None:
        self.image = pygame.transform.scale(self.image, (side_length, side_length))
        self.rect = self.image.get_rect()
        self.rect.x = self.x*side_length
        self.rect.y = self.y*side_length

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
        super().__init__(x, y, img_x, img_y)

        self.status = {}
        self.status["health"] = 100
        self.status["hit_timer"] = 0

        self.images = {}
        self.image = None
        self.__load_images()

        self.rect = self.image.get_rect()
        self.rect.x = img_x
        self.rect.y = img_y

    def update(self, damage: int = None) -> None:
        if damage is not None:
            self._take_damage(damage)
        else:
            self._update_timers()
        self._update_image()

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

    def _take_damage(self, damage: int) -> None:
        self.status["health"] -= damage
        self.status["hit_timer"] = BASE_HIT_TIMER

        if self.status["health"] <= 0:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, custom_type=GAME_OVER))

    def _update_timers(self) -> None:
        if self.status["hit_timer"] > 0:
            self.status["hit_timer"] -= 1

    def _update_image(self) -> None:
        if self.status["hit_timer"] > 0:
            self.image = self.images["hit"]
        else:
            self.image = self.images["normal"]

    def __load_images(self) -> None:
        curdir = os.path.dirname(__file__)
        image_path = os.path.join(curdir, "..", "assets", "tiles", "base.png")
        hit_image_path = os.path.join(curdir, "..", "assets", "tiles", "base_hit.png")

        self.images["normal"] = pygame.image.load(image_path).convert()
        self.images["hit"] = pygame.image.load(hit_image_path).convert()

        self._update_image()
