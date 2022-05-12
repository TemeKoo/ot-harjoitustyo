import pygame
from game_objects.enemy import Enemy
from game_objects.field import Field
from game_objects.tower import Tower
from helpers.level_loader import LevelLoader
from render.renderers import Renderer
from ui.buttons import TowerButton

from logic.event_handler import EventHandler


class GameLoop():
    """Runs the game."""

    def __init__(self, screen):
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.running = False

        self.event_handler = EventHandler()
        self.loader = LevelLoader()

        self.scene_data = {
            "scene": "level_1",
            "scene_type": "level",
            "sprites": pygame.sprite.Group(),
            "towers": pygame.sprite.Group(),
            "enemies": pygame.sprite.Group(),
            "buttons": pygame.sprite.Group(),
            "field": Field(1, self.loader),
            "loader": self.loader,
            "game_over": False,
            "game_over_displayed": False
        }

        self.renderer = Renderer(screen, self.scene_data)

        self.spawn_enemy()

        new_tower = Tower(300, 220)
        self.scene_data["towers"].add(new_tower)
        self.scene_data["sprites"].add(new_tower)

        button = TowerButton(40, 400)
        self.scene_data["buttons"].add(button)
        self.scene_data["sprites"].add(button)

    def loop(self) -> None:
        """Main loop of the game."""
        while self.running:
            self.running = self.event_handler.handle_events(self.scene_data)
            if not self.scene_data["game_over"]:
                self.scene_data["enemies"].update()
                self.scene_data["towers"].update(try_fire=True)
                self.scene_data["field"].update()
                if len(self.scene_data["enemies"]) == 0:
                    self.spawn_enemy()
            elif not self.scene_data["game_over_displayed"]:
                self.game_over()
            self.renderer.render(self.scene_data)
            self.clock.tick(self.fps)

    def game_over(self) -> None:
        """Sets game over screen."""
        self.renderer.set_game_over()

    def run(self) -> None:
        """Runs the game."""
        if not self.running:
            self.renderer.set_scene(self.scene_data)
            self.running = True
            self.loop()

    def spawn_enemy(self) -> None:
        """Spawns an enemy at the start of the path."""
        enemy_path = self.loader.get_path(1)
        new_enemy = Enemy(enemy_path)
        self.scene_data["enemies"].add(new_enemy)
        self.scene_data["sprites"].add(new_enemy)
