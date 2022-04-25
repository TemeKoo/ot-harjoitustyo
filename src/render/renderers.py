import pygame
from game_objects.field import Field


class Renderer():
    def __init__(self, screen: pygame.Surface, scene_data: dict) -> None:
        self.surface = screen
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

        self.scene_data = scene_data

        self.ui_renderer = UiRenderer(0, 0, self.scene_data)
        self.game_renderer = GameRenderer(0, 0, self.scene_data)

        self.__update_renderers()

    def render(self, scene_data: dict) -> None:
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
        game_renderer_height = int(self.height*0.75)
        self.game_renderer.size = self.width, game_renderer_height

    @property
    def screen(self) -> pygame.Surface:
        return self.surface

    @screen.setter
    def screen(self, new_screen: pygame.Surface) -> None:
        self.surface = new_screen
        self.__update_renderers()


class GenericRenderer():
    def __init__(self, width: int, height: int, scene_data: dict) -> None:
        self.width = width
        self.height = height
        self.scene_data = scene_data
        self.scene = None
        self.surface = None

    def set_scene(self, scene: str) -> None:
        self.scene = scene

    def render(self, screen: pygame.Surface) -> None:
        if self.surface is not None:
            screen.blit(self.surface, (0, 0))

    @property
    def size(self) -> tuple:
        return (self.width, self.height)

    @size.setter
    def size(self, size: "tuple[int]") -> None:
        self.width = size[0]
        self.height = size[1]


class UiRenderer(GenericRenderer):
    def __init__(self, width: int, height: int, scene_data: dict) -> None:
        super().__init__(width, height, scene_data)


class GameRenderer(GenericRenderer):
    def __init__(self, width: int, height: int, scene_data: int) -> None:
        super().__init__(width, height, scene_data)
        self.field = None

    def set_scene(self, scene: str, field: Field = None) -> None:
        super().set_scene(scene)
        if field is not None:
            self.field = field
            self.tiles = field.get_tiles()
            self.field_width, self.field_height = field.get_image_size()
        self.update_image()

    def update_image(self) -> None:
        self.surface = pygame.Surface((self.width, self.height))
        self.field_surface = pygame.Surface((self.field_width, self.field_height))
        self.tiles.draw(self.field_surface)
        self.surface = self.surface.convert()
        self.field_surface = self.field_surface.convert()

    def render(self, screen) -> None:
        towers: pygame.sprite.Group = self.scene_data["towers"]
        enemies: pygame.sprite.Group = self.scene_data["enemies"]

        #towers.draw(self.surface)
        #enemies.draw(self.surface)

        self.surface.fill((0, 0, 0))
        self.surface.blit(self.field_surface, (0, 0))

        return super().render(screen)
