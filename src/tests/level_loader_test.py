import unittest

from helpers.level_loader import LevelLoader


class TestLevelLoader(unittest.TestCase):
    def setUp(self):
        self.level_loader = LevelLoader()
        self.level = 1
        self.level_name = "First level"
        self.field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 1, 0, 0, 1, 2, 0],
                      [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.path = [(0, 4), (1, 4), (2, 4), (2, 3), (2, 2), (3, 2), (4, 2),
                     (5, 2), (5, 3), (5, 4), (6, 4), (7, 4), (8, 4), (8, 3), (9, 3)]
        self.wave_number = 1
        self.wave = {"enemies": {"normal": 10}, "cooldown": 1000}

    def test_level_loader_is_created(self):
        self.assertNotEqual(self.level_loader, None)

    def test_get_level_name_works(self):
        self.assertEqual(self.level_loader.get_name(
            self.level), self.level_name)

    def test_get_level_name_returns_none(self):
        self.assertEqual(self.level_loader.get_name(-10), None)

    def test_get_level_field_works(self):
        self.assertEqual(self.level_loader.get_field(self.level), self.field)

    def test_get_level_field_returns_none(self):
        self.assertEqual(self.level_loader.get_field(-10), None)

    def test_get_path_works(self):
        self.assertEqual(self.level_loader.get_path(self.level), self.path)

    def test_get_path_returns_none(self):
        self.assertEqual(self.level_loader.get_path(-10), None)

    def test_get_wave_works(self):
        self.assertEqual(self.level_loader.get_wave(self.level, self.wave_number), self.wave)
    
    def test_get_wave_returns_none(self):
        self.assertEqual(self.level_loader.get_wave(self.level, -10), None)
