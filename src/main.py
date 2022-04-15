import pygame

from logic.game_loop import GameLoop
from game_objects.field import Field
from game_objects.tower import Tower
from helpers.level_loader import LevelLoader
from logic.event_handler import EventHandler
from render.renderers import Renderer
from ui.buttons import TowerButton


def main():
    pygame.init()
    pygame.display.set_caption("game test")

    screen: pygame.Surface = pygame.display.set_mode((640, 480))
    game_loop = GameLoop(screen)
    game_loop.run()


if __name__ == "__main__":
    main()
