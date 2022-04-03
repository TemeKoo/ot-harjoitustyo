import pygame
from game_objects.tower import Tower

def main():
    pygame.init()

    pygame.display.set_caption("test program")

    screen = pygame.display.set_mode((640,480))
    
    tower = Tower(300, 220)
    tower.draw(screen)
    pygame.display.flip()

    running = True
     
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()