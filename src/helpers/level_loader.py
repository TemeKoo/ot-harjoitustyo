import json
import os


class LevelLoader():
    """Loads levels from json file."""

    def __init__(self) -> None:
        curdir = os.path.dirname(__file__)
        json_path = os.path.join(curdir, "..", "assets", "levels.json")
        with open(json_path, encoding="utf8") as json_file:
            self._levels_dict = json.load(json_file)

    def get_name(self, level: int) -> str:
        """Returns the name of the level.

        Args:
            level (int): Level number.

        Returns:
            name (str): Level name.
        """
        level = self.__check_level(level)
        if level:
            return self._levels_dict[level]["name"]
        return None

    def get_field(self, level: int) -> list:
        """Returns the field data of the level.

        Args:
            level (int): Level number.

        Returns
            field_data (list): Level field data.
        """
        level = self.__check_level(level)
        if level is not None:
            return self._levels_dict[level]["field"]
        return None

    def get_path(self, level: int) -> list:
        """Returns the enemy path of the level.

        Args:
          level (int): Level number.

        Returns:
            enemy_path (list): Level enemy path.
        """
        level = self.__check_level(level)
        if level is not None:
            path = self._levels_dict[level]["path"]
            path = [(i[0], i[1]) for i in path]
            return path
        return None

    def get_wave(self, level: int, wave: int) -> dict:
        """Returns wave data.

        Args:
          level (int): Level number.
          wave (int): Wave number.

        Returns:
            wave_data (dict): Wave data.
        """
        level, wave = self.__check_wave(level, wave)
        if level is not None:
            return self._levels_dict[level]["waves"][wave]
        return None

    def __check_level(self, level: int) -> str:
        level = str(level)
        return level if level in self._levels_dict else None

    def __check_wave(self, level: int, wave: int) -> str:
        level = self.__check_level(level)
        wave = str(wave)
        if level is not None and wave in self._levels_dict[level]["waves"]:
            return level, wave
        return None, None
