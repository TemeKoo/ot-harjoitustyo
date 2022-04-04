import pygame
from logic.event_handler import EventHandler
from objects.tower import Tower
from objects.field import Field
from helpers.level_loader import LevelLoader
from render.renderer import Renderer

def main():
    pygame.init()

    pygame.display.set_caption("game test")

    screen: pygame.Surface = pygame.display.set_mode((640,480))

    loader = LevelLoader()

    field = Field(1, loader)

    tower = Tower(300, 220)
    pygame.display.flip()

    towers = pygame.sprite.Group()
    towers.add(tower)

    all_sprites = pygame.sprite.Group()

    all_sprites.add(field)
    for t in towers:
        all_sprites.add(tower)

    event_handler = EventHandler()
    renderer = Renderer(screen)

    running = True
     
    while running:
        running = event_handler.handle_events(towers)
        renderer.render(all_sprites)

if __name__ == "__main__":
    main()