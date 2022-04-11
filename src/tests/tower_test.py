import unittest

from game_objects.tower import Tower


class TestTower(unittest.TestCase):
    def setUp(self):
        self.tower = Tower(0, 0)
    
    def test_tower_is_created(self):
        self.assertNotEqual(self.tower, None)