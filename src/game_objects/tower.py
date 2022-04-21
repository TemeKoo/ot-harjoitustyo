import os

import pygame

TOWER_FIRE = 1
TOWER_RANGE = 1
TOWER_DAMAGE = 20


class Tower(pygame.sprite.Sprite):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__()

        curdir = os.path.dirname(__file__)
        image_path = os.path.join(curdir, "..", "assets", "tower.png")
        firing_image_path = os.path.join(curdir, "..", "assets", "tower_firing.png")
        self.normal_image: pygame.Surface = pygame.image.load(image_path)
        self.firing_image: pygame.Surface = pygame.image.load(firing_image_path)

        self.normal_image = self.normal_image.convert()
        self.firing_image = self.firing_image.convert()

        self.image = self.normal_image

        self.x = x
        self.y = y

        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.grabbed = False
        self.grabbed_rel = (0, 0)

        self.on_tile = False

        self.timer = 0
        self.fire_timer = 0

        self.fire_range = TOWER_RANGE
        self.damage = TOWER_DAMAGE

    def grab(self, mouse_pos) -> None:
        m_x, m_y = mouse_pos
        rel_x = self.rect.x - m_x
        rel_y = self.rect.y - m_y
        self.grabbed_rel = (rel_x, rel_y)
        self.grabbed = True

    def drop(self) -> None:
        self.grabbed = False

    def update(self, pos: tuple = None, on_tile: bool = None, tile_pos: tuple = None, try_fire: bool = False, fire: bool = False) -> None:
        if pos is not None and self.grabbed:
            self.on_tile = on_tile
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
            self.fire_timer = 7
            self.image = self.firing_image

        elif try_fire and self.on_tile:
            self.timer += 1
            if self.timer >= 30:
                self.timer = 0
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, custom_type=TOWER_FIRE, tower=self))
            if self.fire_timer > 0:
                self.fire_timer -= 1
                if self.fire_timer == 0:
                    self.image = self.normal_image

    @property
    def pos(self) -> tuple:
        return (self.x, self.y)

    @pos.setter
    def pos(self, pos) -> None:
        x, y, img_x, img_y = pos
        self.x = x
        self.y = y
        self.rect.x = img_x
        self.rect.y = img_y
