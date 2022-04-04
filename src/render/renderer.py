import pygame

class Renderer():
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
    
    def render(self, sprites: pygame.sprite.Group):
        self.screen.fill((0, 0, 0))
        sprites.draw(self.screen)
        pygame.display.update()