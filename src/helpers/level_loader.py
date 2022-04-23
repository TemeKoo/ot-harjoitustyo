import json
import os


class LevelLoader():
    def __init__(self) -> None:
        curdir = os.path.dirname(__file__)
        json_path = os.path.join(curdir, "..", "assets", "levels.json")
        with open(json_path, encoding="utf8") as json_file:
            self._levels_dict = json.load(json_file)

    def _check_level(self, level: int) -> str:
        level = str(level)
        return level if level in self._levels_dict else None

    def _check_wave(self, level: int, wave: int) -> str:
        level = self._check_level(level)
        wave = str(wave)
        if level is not None and wave in self._levels_dict[level]["waves"]:
            return level, wave
        return None, None

    def get_name(self, level: int) -> str:
        level = self._check_level(level)
        if level:
            return self._levels_dict[level]["name"]
        return None

    def get_field(self, level: int) -> list:
        level = self._check_level(level)
        if level is not None:
            return self._levels_dict[level]["field"]
        return None

    def get_path(self, level: int) -> list:
        level = self._check_level(level)
        if level is not None:
            path = self._levels_dict[level]["path"]
            path = [(i[0], i[1]) for i in path]
            return path
        return None

    def get_wave(self, level: int, wave: int) -> dict:
        level, wave = self._check_wave(level, wave)
        if level is not None:
            return self._levels_dict[level]["waves"][wave]
        return None
