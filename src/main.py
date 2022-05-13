import pygame

from logic.game_loop import GameLoop


def main():
    """Main function of the app."""
    pygame.init()
    pygame.display.set_caption("Tower Defense")

    screen: pygame.Surface = pygame.display.set_mode((640, 480))
    game_loop = GameLoop(screen)
    game_loop.run()


if __name__ == "__main__":
    main()
