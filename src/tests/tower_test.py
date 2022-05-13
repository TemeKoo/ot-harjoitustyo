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

    def test_tower_range_is_correct(self):
        self.assertEqual(self.tower.fire_range, 1)
    
    def test_tower_damage_is_correct(self):
        self.assertEqual(self.tower.damage, 20)

    def test_tower_move_works(self):
        self.tower.grab((0, 0))
        self.tower.update(pos=(0, 1), on_tile=False)
        self.tower.drop()
        self.assertEqual((self.tower.rect.x, self.tower.rect.y), (0, 1))
    
    def test_tower_move_to_tile_works(self):
        self.tower.grab((0, 0))
        self.tower.update(pos=(0, 1), on_tile=True, tile_pos=(0, 0))
        self.tower.drop()
        self.assertEqual(self.tower.pos, (0, 0))

    def test_tower_firing_works(self):
        self.tower.grab((0,0))
        self.tower.update(try_fire=True)
        self.tower.update(pos=(0, 1), on_tile=True, tile_pos=(0, 0))
        self.tower.drop()
        self.tower.update(try_fire=True)
        self.tower.update(fire=True)
        for _ in range(10):
            self.tower.update(try_fire=True)
        self.assertEqual(self.tower.status["cooldown"], 20)