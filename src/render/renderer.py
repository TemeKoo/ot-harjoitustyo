import pygame

class Renderer():
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
    
    def render(self, scene_data: dict):
        sprites = scene_data["sprites"]
        self.screen.fill((0, 0, 0))
        sprites.draw(self.screen)
        pygame.display.update()