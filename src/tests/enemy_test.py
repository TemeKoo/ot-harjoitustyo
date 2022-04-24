import os
import unittest

import pygame
from game_objects.enemy import Enemy
from helpers.level_loader import LevelLoader


class TestEnemy(unittest.TestCase):
    def setUp(self):
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        pygame.display.init()
        pygame.display.set_mode((1, 1))
        self.loader = LevelLoader()
        enemy_path = self.loader.get_path(1)
        self.tower_pos = enemy_path[0]
        self.tower_range = 1
        self.enemy = Enemy(enemy_path)

    def test_enemy_is_created(self):
        self.assertNotEqual(self.enemy, None)

    def test_enemy_is_hit(self):
        self.assertEqual(self.enemy.hit(self.tower_pos, self.tower_range), True)

    def test_enemy_is_not_hit_x(self):
        self.assertEqual(self.enemy.hit((10, 0), 1), False)

    def test_enemy_is_not_hit_y(self):
        self.assertEqual(self.enemy.hit((0, 0), 1), False)

    def test_enemy_update(self):
        self.enemy.update()
        self.enemy.update(20)
        for _ in range(10000):
            self.enemy.update()
        self.enemy.update(100)
        for _ in range(100):
            self.enemy.update()
    
    def test_enemy_dies(self):
        self.enemy.update(100)
        self.enemy.update()
        self.assertEqual(self.enemy.dying, True)
