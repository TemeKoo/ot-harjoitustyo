import os
import unittest

import pygame
from game_objects.tower import Tower
from ui.buttons import MenuButton, TowerButton


class TestTowerButton(unittest.TestCase):
    def setUp(self):
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        pygame.display.init()
        pygame.display.set_mode((1, 1))
        self.button = TowerButton(0, 0)

    def test_button_is_created(self):
        self.assertNotEqual(self.button, None)

    def test_click_returns_tower(self):
        self.assertEqual(type(self.button.click((0, 0))), Tower)


class TestMenuButton(unittest.TestCase):
    pass
