import pygame
from game_objects.tower import Tower
from ui.buttons import TowerButton


class EventHandler():
    def __init__(self):
        self.mouse_down = False
        self.dragged_towers = pygame.sprite.Group()

    def handle_events(self, scene_data: dict):
        sprites = scene_data["sprites"]
        sprites_to_add = pygame.sprite.Group()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_down = True
                    for sprite in sprites:
                        if isinstance(sprite, Tower) and sprite.rect.collidepoint(event.pos):
                            tower = sprite
                            tower.grab(event.pos)
                            self.dragged_towers.add(tower)

                        if isinstance(sprite, TowerButton) and sprite.rect.collidepoint(event.pos):
                            button = sprite
                            new_tower = button.click(event.pos)
                            sprites_to_add.add(new_tower)
                            new_tower.grab(event.pos)
                            self.dragged_towers.add(new_tower)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_down = False
                    for tower in self.dragged_towers:
                        tower.drop()

        if self.mouse_down:
            mouse_pos = pygame.mouse.get_pos()
            sprites.update(mouse_pos=mouse_pos)

        if len(sprites_to_add.sprites()) > 0:
            for sprite in sprites_to_add:
                scene_data["sprites"].add(sprite)
            sprites_to_add.empty()

        return True
