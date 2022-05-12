import pygame
from game_objects.field import Field


class Renderer():
    """Main renderer of the game."""

    def __init__(self, screen: pygame.Surface, scene_data: dict) -> None:
        self.surface = screen
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

        self.scene_data = scene_data

        self.ui_renderer = UiRenderer(0, 0, self.scene_data)
        self.game_renderer = GameRenderer(0, 0, self.scene_data)

        self.__update_renderers()

        self.text_surface = None

    def render(self, scene_data: dict) -> None:
        """Renders the frame.

        Args:
            scene_data (dict)
        """
        sprites = scene_data["sprites"]
        self.surface.fill((0, 0, 0))
        self.game_renderer.render(self.surface)
        sprites.draw(self.surface)
        if self.text_surface is not None:
            text_x = int((self.width - self.text_surface.get_width()) / 2)
            text_y = int((self.height - self.text_surface.get_height()) / 2)
            self.surface.blit(self.text_surface, (text_x, text_y))
        pygame.display.update()

    def set_scene(self, scene_data: dict) -> None:
        """Sets scene.

        Args:
            scene_data (dict)
        """
        self.scene_data = scene_data
        scene = self.scene_data["scene"]
        scene_type = self.scene_data["scene_type"]
        self.ui_renderer.set_scene(scene)
        if scene_type == "level":
            field = scene_data["field"]
            self.game_renderer.set_scene(scene, field)
        else:
            self.game_renderer.set_scene(scene)

    def set_game_over(self) -> None:
        """Sets game over screen."""
        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 50)
        self.text_surface = font.render("Game over!", False, (255, 255, 255))

    def __update_renderers(self) -> None:
        game_renderer_height = int(self.height*0.75)
        self.game_renderer.size = self.width, game_renderer_height

    @property
    def screen(self) -> pygame.Surface:
        """Returns set screen of the renderer.

        Returns:
            screen (pygame.Surface)
        """
        return self.surface

    @screen.setter
    def screen(self, new_screen: pygame.Surface) -> None:
        """Sets screen of the renderer.

        Args:
            new_screen (pygame.Surface) 
        """
        self.surface = new_screen
        self.__update_renderers()


class GenericRenderer():
    """Base for ui and game renderers."""

    def __init__(self, width: int, height: int, scene_data: dict) -> None:
        self.width = width
        self.height = height
        self.scene_data = scene_data
        self.scene = None
        self.surface = None

    def set_scene(self, scene: str) -> None:
        """Sets scene.

        Args:
            scene_data (dict)
        """
        self.scene = scene

    def render(self, screen: pygame.Surface) -> None:
        """Draws the surface of the renderer.

        Args:
            screen (pygame.Surface): Screen to draw on.
        """
        if self.surface is not None:
            screen.blit(self.surface, (0, 0))

    @property
    def size(self) -> tuple:
        """Returns the size of the surface of the renderer.

        Returns:
            size (tuple): (width, height) in pixels.
        """
        return (self.width, self.height)

    @size.setter
    def size(self, size: "tuple[int]") -> None:
        """Sets the size of the surface of the renderer.

        Args:
          size (tuple): wanted size of surface in tuple (width, height).
        """
        self.width = size[0]
        self.height = size[1]


class UiRenderer(GenericRenderer):
    """Class to render the ui."""

    def __init__(self, width: int, height: int, scene_data: dict) -> None:
        super().__init__(width, height, scene_data)


class GameRenderer(GenericRenderer):
    """Class to render the game."""

    def __init__(self, width: int, height: int, scene_data: int) -> None:
        super().__init__(width, height, scene_data)
        self.field = None

    def set_scene(self, scene: str, field: Field = None) -> None:
        """Sets scene.

        Args:
          scene (str) 
          field (game_objects.field.Field): The current field. (Default value = None)
        """
        super().set_scene(scene)
        if field is not None:
            self.field = field
            self.tiles = field.get_tiles()
            self.field_width, self.field_height = field.get_image_size()
        self.__update_image()

    def __update_image(self) -> None:
        self.surface = pygame.Surface((self.width, self.height))
        self.field_surface = pygame.Surface(
            (self.field_width, self.field_height))
        self.tiles.draw(self.field_surface)
        self.surface = self.surface.convert()
        self.field_surface = self.field_surface.convert()

    def render(self, screen) -> None:
        """Draws the surface of the renderer.

        Args:
            screen (pygame.Surface): Screen to draw on.
        """
        base_tile = self.field.get_base_tile()

        self.surface.fill((0, 0, 0))
        self.surface.blit(self.field_surface, (0, 0))
        base_tile.draw(self.surface)

        return super().render(screen)
