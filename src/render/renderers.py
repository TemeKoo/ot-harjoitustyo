import pygame


class Renderer():
    def __init__(self, screen: pygame.Surface):
        self.surface = screen
        self.ui_renderer = UiRenderer(0, 0)
        self.game_renderer = GameRenderer(0, 0)
        self.scene_data = None
    
    def render(self, scene_data: dict):
        sprites = scene_data["sprites"]
        self.surface.fill((0, 0, 0))
        sprites.draw(self.surface)
        pygame.display.update()
    
    def set_scene(self, scene_data: dict) -> None:
        self.scene_data = scene_data
        scene = self.scene_data["scene"]
        scene_type = self.scene_data["scene_type"]
        self.ui_renderer.set_scene(scene)
        if scene_type == "level":
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

    def set_scene(self, scene: str) -> None:
        self.scene = scene

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
