import os

import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__()

        curdir = os.path.dirname(__file__)
        image_path = os.path.join(curdir, "..", "assets", "tower.png")
        self.image: pygame.Surface = pygame.image.load(image_path)

        self.image = self.image.convert()

        self.x = x
        self.y = y

        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.grabbed = False
        self.grabbed_rel = (0, 0)

    def grab(self, mouse_pos) -> None:
        m_x, m_y = mouse_pos
        rel_x = self.x - m_x
        rel_y = self.y - m_y
        self.grabbed_rel = (rel_x, rel_y)
        self.grabbed = True

    def drop(self) -> None:
        self.grabbed = False

    def update(self, mouse_pos: tuple) -> None:
        if self.grabbed:
            m_x, m_y = mouse_pos
            rel_x, rel_y = self.grabbed_rel
            x = m_x + rel_x
            y = m_y + rel_y
            self.pos = x, y

    @property
    def pos(self) -> tuple:
        return (self.x, self.y)

    @pos.setter
    def pos(self, pos) -> None:
        x, y = pos
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def scale_to(self, times):
        pass
