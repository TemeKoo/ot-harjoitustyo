import os

import pygame

GAME_OVER = 3
BASE_HIT_TIMER = 12


class GenericTile(pygame.sprite.Sprite):
    """Generic class to represent one tile of the playing field."""

    def __init__(self, x, y, img_x, img_y, image_name: str = None):
        super().__init__()

        self.x = x
        self.y = y

        if image_name is not None:
            curdir = os.path.dirname(__file__)
            image_path = os.path.join(
                curdir, "..", "assets", "tiles", image_name)
            self.image = pygame.image.load(image_path)

            self.rect = self.image.get_rect()
            self.rect.x = img_x
            self.rect.y = img_y

    def scale(self, side_length: int) -> None:
        """Scales the tile.

        Args:
            side_length (int): Wanted side length of tile in pixels.
        """
        self.image = pygame.transform.scale(
            self.image, (side_length, side_length))
        self.rect = self.image.get_rect()
        self.rect.x = self.x*side_length
        self.rect.y = self.y*side_length

    def get_pos(self) -> tuple:
        """Returns the field position of the tile.

        Returns:
            pos (tuple): (x, y)
        """
        return (self.x, self.y)

    def get_img_pos(self) -> tuple:
        """Returns the image position of the tile.

        Returns:
            pos (tuple): (x, y)
        """
        return (self.rect.x, self.rect.y)


class PathTile(GenericTile):
    """A tile on which enemies move."""

    def __init__(self, x, y, img_x, img_y):
        image_name = "path.png"
        super().__init__(x, y, img_x, img_y, image_name=image_name)


class BuildableTile(GenericTile):
    """A tile on which towers can be built."""

    def __init__(self, x, y, img_x, img_y):
        image_name = "buildable.png"
        super().__init__(x, y, img_x, img_y, image_name=image_name)


class BaseTile(GenericTile):
    """A tile which is the base of the player."""

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
        """Override of the pygame update function.
        Use without arguments once per frame to update cooldowns.

        Args:
            damage (int): The base takes this amount of damage. (Default value = None)
        """
        if damage is not None:
            self.__take_damage(damage)
        else:
            self.__update_timers()

        self.__update_image()

    def draw(self, surface: pygame.Surface):
        """Implementation of the pygame draw function.

        Args:
            surface (pygame.Surface): The surface on which to draw.
        """
        surface.blit(self.image, self.rect)

    def __take_damage(self, damage: int) -> None:
        self.status["health"] -= damage
        self.status["hit_timer"] = BASE_HIT_TIMER

        if self.status["health"] <= 0:
            pygame.event.post(pygame.event.Event(
                pygame.USEREVENT, custom_type=GAME_OVER))

    def __update_timers(self) -> None:
        if self.status["hit_timer"] > 0:
            self.status["hit_timer"] -= 1

    def __update_image(self) -> None:
        if self.status["hit_timer"] > 0:
            self.image = self.images["hit"]
        else:
            self.image = self.images["normal"]

    def __load_images(self) -> None:
        curdir = os.path.dirname(__file__)
        image_path = os.path.join(curdir, "..", "assets", "tiles", "base.png")
        hit_image_path = os.path.join(
            curdir, "..", "assets", "tiles", "base_hit.png")

        self.images["normal"] = pygame.image.load(image_path).convert()
        self.images["hit"] = pygame.image.load(hit_image_path).convert()

        self.__update_image()
