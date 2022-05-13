import pygame
from game_objects.tower import Tower
from ui.buttons import TowerButton

from logic.tower_placement import TowerPlacer
from logic.tower_shooting import TowerShooter

TOWER_FIRE = 1
BASE_DAMAGED = 2
GAME_OVER = 3


class EventHandler():
    """A class to handle relevant events in the pygame event queue."""

    def __init__(self):
        self.mouse_down = False

        self.tower_placer = TowerPlacer()
        self.dragged_towers = pygame.sprite.Group()
        self.sprites_to_add = pygame.sprite.Group()

        self.tower_shooter = TowerShooter()

    def handle_events(self, scene_data: dict):
        """Main method to handle events.

        Args:
            scene_data (dict): Scene data.

        Returns:
            running (bool): Is False if pygame.QUIT was encountered, otherwise True.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouse_button_down(scene_data["sprites"], event)

            elif event.type == pygame.MOUSEBUTTONUP:
                self.__mouse_button_up(event)

            elif event.type == pygame.USEREVENT:
                if event.custom_type == TOWER_FIRE:
                    self.tower_shooter.fire_tower(
                        event.tower, scene_data["enemies"])

                elif event.custom_type == BASE_DAMAGED:
                    scene_data["field"].update(base_damage=event.damage)

                elif event.custom_type == GAME_OVER:
                    scene_data["game_over"] = True

        self.__handle_towers(scene_data)
        self.__add_sprites(scene_data)

        return True

    def __add_sprites(self, scene_data: dict) -> None:
        if len(self.sprites_to_add.sprites()) > 0:
            for sprite in self.sprites_to_add:
                if isinstance(sprite, Tower):
                    scene_data["towers"].add(sprite)
                scene_data["sprites"].add(sprite)
            self.sprites_to_add.empty()

    def __handle_towers(self, scene_data: dict) -> None:
        if self.mouse_down:
            mouse_pos = pygame.mouse.get_pos()
            self.tower_placer.place_towers(
                scene_data["towers"], scene_data["field"], mouse_pos)

    def __mouse_button_down(self, sprites, event):
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

    def __mouse_button_up(self, event):
        if event.button == 1:
            self.mouse_down = False
            for tower in self.dragged_towers:
                tower.drop()
