import pygame
from game_objects.field import Field


class Renderer():
    def __init__(self, screen: pygame.Surface):
        self.surface = screen
        self.ui_renderer = UiRenderer(0, 0)
        self.game_renderer = GameRenderer(0, 0)
        self.scene_data = None

    def render(self, scene_data: dict):
        sprites = scene_data["sprites"]
        self.surface.fill((0, 0, 0))
        self.game_renderer.render(self.surface)
        sprites.draw(self.surface)
        pygame.display.update()

    def set_scene(self, scene_data: dict) -> None:
        self.scene_data = scene_data
        scene = self.scene_data["scene"]
        scene_type = self.scene_data["scene_type"]
        self.ui_renderer.set_scene(scene)
        if scene_type == "level":
            field = scene_data["field"]
            self.game_renderer.set_scene(scene, field)
        else:
            self.game_renderer.set_scene(scene)

    def __update_renderers(self) -> None:
        pass

    @property
    def screen(self) -> pygame.Surface:
        return self.surface

    @screen.setter
    def screen(self, new_screen: pygame.Surface) -> None:
        self.surface = new_screen
        self.__update_renderers()


class GenericRenderer():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.scene = None
        self.surface = None

    def set_scene(self, scene: str) -> None:
        self.scene = scene

    def render(self, screen: pygame.Surface):
        if self.surface is not None:
            screen.blit(self.surface, (0,0))

    @property
    def size(self) -> tuple:
        return (self.width, self.height)

    @size.setter
    def size(self, width: int, height: int) -> None:
        self.width = width
        self.height = height


class UiRenderer(GenericRenderer):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)


class GameRenderer(GenericRenderer):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)

    def set_scene(self, scene: str, field: Field = None) -> None:
        super().set_scene(scene)
        if field is not None:
            self.tiles = field.get_tiles()
            self.width, self.height = field.get_image_size()
        self.update_image()
    
    def update_image(self):
        self.surface = pygame.Surface((self.width, self.height))
        self.tiles.draw(self.surface)
        self.surface = self.surface.convert()

    def render(self, screen):
        return super().render(screen)