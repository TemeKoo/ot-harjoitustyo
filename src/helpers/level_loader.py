import json
import os


class LevelLoader():
    def __init__(self) -> None:
        curdir = os.path.dirname(__file__)
        json_path = os.path.join(curdir, "..", "assets", "levels.json")
        with open(json_path) as json_file: 
            self._levels_dict = json.load(json_file)

    def _check_level(self, level: int) -> str:
        level = str(level)
        if level in self._levels_dict:
            return level
        else:
            return None

    def get_name(self, level: int) -> str:
        level = self._check_level(level)
        if level:
            return self._levels_dict[level]["name"]
        else:
            return None

    def get_field(self, level: int) -> list:
        level = self._check_level(level)
        if level:
            return self._levels_dict[level]["field"]
        else:
            return None




if __name__ == "__main__":
    loader = LevelLoader()
    print(loader.get_name(1))
    for row in loader.get_field(1):
        print(row)