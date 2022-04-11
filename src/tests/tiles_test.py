import unittest

from game_objects.tiles import BaseTile, BuildableTile, PathTile


class TestBuildableTile(unittest.TestCase):
    def setUp(self):
        self.tile = BuildableTile(0, 0, 0, 0)

    def test_tile_is_created(self):
        self.assertNotEqual(self.tile, None)

    def test_tile_pos_correct(self):
        self.assertEqual(self.tile.get_pos(), (0, 0))

    def test_tile_img_pos_correct(self):
        self.assertEqual(self.tile.get_img_pos(), (0, 0))


class TestBaseTile(unittest.TestCase):
    def setUp(self):
        self.tile = BaseTile(0, 0, 0, 0)

    def test_tile_is_created(self):
        self.assertNotEqual(self.tile, None)

    def test_tile_pos_correct(self):
        self.assertEqual(self.tile.get_pos(), (0, 0))

    def test_tile_img_pos_correct(self):
        self.assertEqual(self.tile.get_img_pos(), (0, 0))


class TestPathTile(unittest.TestCase):
    def setUp(self):
        self.tile = PathTile(0, 0, 0, 0)

    def test_tile_is_created(self):
        self.assertNotEqual(self.tile, None)

    def test_tile_pos_correct(self):
        self.assertEqual(self.tile.get_pos(), (0, 0))

    def test_tile_img_pos_correct(self):
        self.assertEqual(self.tile.get_img_pos(), (0, 0))
