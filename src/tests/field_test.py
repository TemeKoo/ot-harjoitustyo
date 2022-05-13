import os
import unittest

import pygame
from game_objects.field import Field
from helpers.level_loader import LevelLoader

class TestField(unittest.TestCase):
    def setUp(self):
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        pygame.display.init()
        pygame.display.set_mode((1, 1))

        self.field = Field(1, LevelLoader())

    def test_field_is_created(self):
        self.assertNotEqual(self.field, None)
    
    def test_field_update_works(self):
        self.field.update(10)
        self.assertEqual(self.field.get_base_tile().status["health"], 90)
    
    def test_image_size_correct(self):
        self.assertEqual(self.field.get_image_size(), (220, 140))