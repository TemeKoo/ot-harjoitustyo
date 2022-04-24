import os
import unittest

import pygame
from game_objects.tower import Tower


class TestTower(unittest.TestCase):
    def setUp(self):
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        pygame.display.init()
        pygame.display.set_mode((1, 1))
        self.tower = Tower(0, 0)

    def test_tower_is_created(self):
        self.assertNotEqual(self.tower, None)
