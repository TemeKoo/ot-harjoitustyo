import pygame
from logic.event_handler import EventHandler
from logic.level import Level
from render.renderer import Renderer
from helpers.level_loader import LevelLoader


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
            "placing_tower": None,
            "tower_placement_valid": False
        }

    def loop(self):
        while self.running:
            self.running = self.event_handler.handle_events(self.scene_data["sprites"])
            self.renderer.render(self.scene_data)
            self.clock.tick(self.fps)

    def run(self):
        if not self.running:
            self.running = True
            self.loop()
