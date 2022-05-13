import pygame

from game_objects.sprite import GenericSprite

TOWER_FIRE = 1
TOWER_RANGE = 1
TOWER_DAMAGE = 20


class Tower(GenericSprite):
    """Represents a simple tower."""

    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__()

        self.status = {
            "cooldown": 0,
            "firing_effect_timer": 0,
            "firing": False,
            "on_tile": False
        }

        images = {
            "normal": ["tower.png"],
            "firing": ["tower_firing.png"]
        }

        self.load_images(images)
        self.__update_image()

        self.x = x
        self.y = y

        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.grabbed = False
        self.grabbed_rel = (0, 0)

    @property
    def fire_range(self):
        """The fire range of the tower in tiles.
        
        Returns:
            fire_range (int)
        """
        return TOWER_RANGE

    @property
    def damage(self):
        """The damage of the tower.
        
        Returns:
            damage (int)
        """
        return TOWER_DAMAGE

    def grab(self, mouse_pos: tuple) -> None:
        """Used to grab the tower with the mouse.

        Args:
            mouse_pos (tuple): Position of the mouse in tuple (x, y).
        """
        m_x, m_y = mouse_pos
        rel_x = self.rect.x - m_x
        rel_y = self.rect.y - m_y
        self.grabbed_rel = (rel_x, rel_y)
        self.grabbed = True

    def drop(self) -> None:
        """Drops the tower from the mouse."""
        self.grabbed = False

    def update(
        self, pos: tuple = None, on_tile: bool = None,
        tile_pos: tuple = None, try_fire: bool = False,
        fire: bool = False
        ) -> None:
        """Override of the pygame update function.

        Args:
            pos (tuple): Used to move the tower when grabbed. Tuple (x, y). (Default value = None)
            on_tile (bool): Used to specify if the tower is currently on a tile or not. If True, tile_pos is required. (Default value = None)
            tile_pos (tuple): Used to specify the tile the tower is on. (Default value = None)
            try_fire (bool): Try to fire the tower. (Default value = False)
            fire (bool): Used when the tower was fired. (Default value = False)
        """
        if pos is not None and self.grabbed:
            self.status["on_tile"] = on_tile
            if on_tile:
                x, y = tile_pos
                img_x, img_y = pos
            else:
                x, y = -1, -1
                mouse_x, mouse_y = pos
                rel_x, rel_y = self.grabbed_rel
                img_x = mouse_x + rel_x
                img_y = mouse_y + rel_y
            self.pos = x, y, img_x, img_y

        elif fire:
            self.status["firing_effect_timer"] = 7
            self.status["firing"] = True
            self.__update_image()

        elif try_fire:
            if self.status["cooldown"] > 0:
                self.status["cooldown"] -= 1
            elif self.status["on_tile"]:
                self.status["cooldown"] = 30
                pygame.event.post(pygame.event.Event(
                    pygame.USEREVENT, custom_type=TOWER_FIRE, tower=self))

            if self.status["firing_effect_timer"] > 0:
                self.status["firing_effect_timer"] -= 1
                if self.status["firing_effect_timer"] == 0:
                    self.status["firing"] = False
                    self.__update_image()

    def scale(self, side_length: int) -> None:
        """Scales the tower.

        Args:
            side_length (int): Wanted side length of the tower in pixels.
        """
        for key, image in self.images.items():
            self.images[key] = pygame.transform.scale(
                image, (side_length, side_length))
        self.__update_image()
        self.rect = self.image.get_rect()

    @property
    def pos(self) -> tuple:
        """Returns the x, y coordinates of the tower."""
        return (self.x, self.y)

    @pos.setter
    def pos(self, pos: tuple) -> None:
        """Sets the position of the tower.

        Args:
            pos (tuple): Position to set the tower to. In form (x, y, img_x, img_y).
        """
        x, y, img_x, img_y = pos
        self.x = x
        self.y = y
        self.rect.x = img_x
        self.rect.y = img_y

    def __update_image(self) -> None:
        if self.status["firing"]:
            self.image = self.images["firing"]
        else:
            self.image = self.images["normal"]
