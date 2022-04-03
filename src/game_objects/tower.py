import pygame
import os

curdir = os.path.dirname(__file__)

class Tower(pygame.Sprite):
    def __init__(self, x: int = 0, y: int = 0):
        super().__init__()

        self.texture: pygame.Surface = pygame.image.load(os.path.join(curdir, "..", "assets", "tower.png"))
    
        self.bounding_box: pygame.Rect = self.texture.get_rect()

        self.x = x
        self.y = y


    def draw(self, surface: pygame.Surface):
        surface.blit(self.texture, (self.x, self.y))
    
    def scale_to(self, times):
        pass
