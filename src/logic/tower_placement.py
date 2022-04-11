import pygame
from game_objects.field import Field
from game_objects.tiles import GenericTile


class MousePoint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 1, 1)


class TowerPlacer():
    def __init__(self):
        pass

    def place_towers(self, towers: pygame.sprite.Group, field: Field, mouse_pos: tuple):
        mouse_x, mouse_y = mouse_pos
        colliding_tiles = pygame.sprite.spritecollide(
            MousePoint(mouse_x, mouse_y), field.get_tiles(), False)
        if len(colliding_tiles) > 0:
            colliding_tile: GenericTile = colliding_tiles[0]
            pos = colliding_tile.get_img_pos()
            on_tile = True
            tile_pos = colliding_tile.get_pos()
            towers.update(pos, on_tile, tile_pos)
        else:
            pos = mouse_pos
            on_tile = False
            towers.update(pos, on_tile)
