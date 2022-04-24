import pygame
from game_objects.enemy import Enemy
from game_objects.field import Field
from game_objects.tower import Tower
from helpers.level_loader import LevelLoader
from render.renderers import Renderer
from ui.buttons import TowerButton

from logic.event_handler import EventHandler


class GameLoop():
    def __init__(self, screen):
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.running = False

        self.event_handler = EventHandler()
        self.renderer = Renderer(screen)
        self.loader = LevelLoader()

        self.scene_data = {
            "scene": "level_1",
            "scene_type": "level",
            "sprites": pygame.sprite.Group(),
            "towers": pygame.sprite.Group(),
            "enemies": pygame.sprite.Group(),
            "field": Field(1, self.loader),
            "loader": self.loader
        }

        self.spawn_enemy()

        new_tower = Tower(300, 220)
        self.scene_data["towers"].add(new_tower)
        self.scene_data["sprites"].add(new_tower)

        self.scene_data["sprites"].add(TowerButton(40, 400))

    def loop(self):
        while self.running:
            self.running = self.event_handler.handle_events(self.scene_data)
            self.scene_data["enemies"].update()
            self.scene_data["towers"].update(try_fire=True)
            if len(self.scene_data["enemies"]) == 0:
                self.spawn_enemy()
            self.renderer.render(self.scene_data)
            self.clock.tick(self.fps)

    def run(self):
        if not self.running:
            self.renderer.set_scene(self.scene_data)
            self.running = True
            self.loop()

    def spawn_enemy(self):
        enemy_path = self.loader.get_path(1)
        new_enemy = Enemy(enemy_path)
        self.scene_data["enemies"].add(new_enemy)
        self.scene_data["sprites"].add(new_enemy)
