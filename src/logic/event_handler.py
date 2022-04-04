import pygame

class EventHandler():
    def __init__(self):
        self.mouse_down = False
        self.dragged_towers = pygame.sprite.Group()

    def handle_events(self, sprites: pygame.sprite.Group):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_down = True
                    for sprite in sprites:
                        if tower.collides_with(event.pos):
                            self.dragged_towers.add(tower)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_down = False
                    self.dragged_towers.empty()

        if self.mouse_down:
            for tower in self.dragged_towers:
                tower.pos = pygame.mouse.get_pos()

        return True