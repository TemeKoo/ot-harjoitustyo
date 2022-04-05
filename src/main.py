import pygame
from logic.event_handler import EventHandler
from game_objects.tower import Tower
from game_objects.field import Field
from helpers.level_loader import LevelLoader
from render.renderers import Renderer

from ui.buttons import TowerButton


def main():
    pygame.init()

    pygame.display.set_caption("game test")

    screen: pygame.Surface = pygame.display.set_mode((640,480))

    loader = LevelLoader()

    field = Field(1, loader)

    tower = Tower(300, 220)

    towers = pygame.sprite.Group()
    towers.add(tower)

    all_sprites = pygame.sprite.Group()

    all_sprites.add(field)
    for t in towers:
        all_sprites.add(t)

    button = TowerButton(40, 400)
    all_sprites.add(button)

    event_handler = EventHandler()
    renderer = Renderer(screen)

    scene_data = {
        "sprites": all_sprites
    }

    clock = pygame.time.Clock()

    running = True
    while running:
        running = event_handler.handle_events(scene_data)
        renderer.render(scene_data)
        clock.tick(30)

if __name__ == "__main__":
    main()