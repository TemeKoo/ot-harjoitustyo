import pygame
from game_objects.tower import Tower


class TowerShooter():
    """Handles towers shooting enemies."""

    def fire_tower(self, tower: Tower, enemies: pygame.sprite.Group) -> None:
        """Fires one tower.

        Args:
            tower (game_objects.tower.Tower): The tower to be fired.
            enemies (pygame.sprite.Group): All enemies.
        """
        hit_enemies = pygame.sprite.Group(
            [enemy for enemy in enemies
             if not enemy.dying and enemy.hit(tower.pos, tower.fire_range)])
        hit_enemies.update(damage=tower.damage)
        if len(hit_enemies) > 0:
            tower.update(fire=True)
