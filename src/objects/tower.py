import pygame
import os

class Tower(pygame.sprite.Sprite):
    def __init__(self, x: int = 0, y: int = 0):
        super().__init__()

        curdir = os.path.dirname(__file__)
        self.image: pygame.Surface = pygame.image.load(os.path.join(curdir, "..", "assets", "tower.png"))

        self.image = self.image.convert()

        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def collides_with(self, pos):
        return self.rect.collidepoint(pos)

    def update(self):
        pass

    @property
    def pos(self):
        return (self.x, self.y)
    
    @pos.setter
    def pos(self, pos):
        x, y = pos
        self.rect.x = x
        self.rect.y = y
    
    def scale_to(self, times):
        pass
