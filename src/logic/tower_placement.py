import pygame
from game_objects.field import Field
from game_objects.tiles import GenericTile
from game_objects.tiles import BuildableTile


class MousePoint(pygame.sprite.Sprite):
    """Class to help with mouse collision."""

    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 1, 1)


class TowerPlacer():
    """Handles tower placement."""

    def place_towers(self, towers: pygame.sprite.Group, field: Field, mouse_pos: tuple) -> None:
        """Moves towers.

        Args:
            towers (pygame.sprite.Group): All towers.
            field (game_objects.field.Field): The current field.
            mouse_pos (tuple): Position of the mouse.
        """
        mouse_x, mouse_y = mouse_pos
        colliding_tiles = pygame.sprite.spritecollide(
            MousePoint(mouse_x, mouse_y), field.get_tiles(), False)
        if len(colliding_tiles) > 0:
            colliding_tile: GenericTile = colliding_tiles[0]
            if isinstance(colliding_tile, BuildableTile):
                pos = colliding_tile.get_img_pos()
                on_tile = True
                tile_pos = colliding_tile.get_pos()
                towers.update(pos=pos, on_tile=on_tile, tile_pos=tile_pos)
        else:
            pos = mouse_pos
            on_tile = False
            towers.update(pos=pos, on_tile=on_tile)
