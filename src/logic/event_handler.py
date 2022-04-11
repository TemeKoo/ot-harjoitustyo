import pygame
from game_objects.tower import Tower
from ui.buttons import TowerButton

from logic.tower_placement import TowerPlacer


class EventHandler():
    def __init__(self):
        self.tower_placer = TowerPlacer()
        self.mouse_down = False
        self.dragged_towers = pygame.sprite.Group()

    def handle_events(self, scene_data: dict):
        sprites = scene_data["sprites"]
        field = scene_data["field"]
        towers = scene_data["towers"]
        sprites_to_add = pygame.sprite.Group()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down(sprites, sprites_to_add, event)

            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_up(event)

        if self.mouse_down:
            mouse_pos = pygame.mouse.get_pos()
            self.tower_placer.place_towers(towers, field, mouse_pos)

        if len(sprites_to_add.sprites()) > 0:
            for sprite in sprites_to_add:
                if isinstance(sprite, Tower):
                    scene_data["towers"].add(sprite)
                scene_data["sprites"].add(sprite)
            sprites_to_add.empty()

        return True

    def mouse_button_down(self, sprites, sprites_to_add, event):
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

    def mouse_button_up(self, event):
        if event.button == 1:
            self.mouse_down = False
            for tower in self.dragged_towers:
                tower.drop()
