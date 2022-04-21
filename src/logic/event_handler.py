import pygame
from game_objects.tower import Tower
from game_objects.field import Field
from ui.buttons import TowerButton

from logic.tower_placement import TowerPlacer
from logic.tower_shooting import TowerShooter

TOWER_FIRE = 1


class EventHandler():
    def __init__(self):
        self.mouse_down = False

        self.tower_placer = TowerPlacer()
        self.dragged_towers = pygame.sprite.Group()
        self.sprites_to_add = pygame.sprite.Group()

        self.tower_shooter = TowerShooter()

    def handle_events(self, scene_data: dict):
        sprites: pygame.sprite.Group = scene_data["sprites"]
        field: Field = scene_data["field"]
        towers: pygame.sprite.Group = scene_data["towers"]
        enemies: pygame.sprite.Group = scene_data["enemies"]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down(sprites, event)

            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_up(event)

            elif event.type == pygame.USEREVENT:
                if event.custom_type == TOWER_FIRE:
                    self.tower_shooter.fire_tower(event.tower, enemies)

        if self.mouse_down:
            mouse_pos = pygame.mouse.get_pos()
            self.tower_placer.place_towers(towers, field, mouse_pos)

        if len(self.sprites_to_add.sprites()) > 0:
            for sprite in self.sprites_to_add:
                if isinstance(sprite, Tower):
                    scene_data["towers"].add(sprite)
                scene_data["sprites"].add(sprite)
            self.sprites_to_add.empty()

        return True

    def mouse_button_down(self, sprites, event):
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
                    self.sprites_to_add.add(new_tower)
                    new_tower.grab(event.pos)
                    self.dragged_towers.add(new_tower)

    def mouse_button_up(self, event):
        if event.button == 1:
            self.mouse_down = False
            for tower in self.dragged_towers:
                tower.drop()
