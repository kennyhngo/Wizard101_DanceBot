import os
from typing import List
from textures import *


class Globals:
    """For threads to share a common variable, since globals do not work."""
    q_pressed = False


def separate(string: str, delimiter="=") -> List[str]:
    """Splits the string into 2 parts based on the separater symbol."""
    idx = string.find(delimiter)
    return [
        string[:idx if idx != -1 else len(string)],
        string[idx+1:] if idx != -1 else ""
    ]


class Properties(object):
    def __init__(self) -> None:
        self.filename = "properties.txt"
        self.screen = [0, 0, 1920, 1080]  # X, Y, Width, Height
        self.screen_scale = 1.0
        while os.getcwd().split("\\")[-1] != "Wiz101_DanceBot":
            os.chdir("..")

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])})"

    def load_file(self, resolution: str = None) -> None:
        """Creates a properties file if one is not found."""
        if not os.path.exists(self.filename):
            self.save_file()
            return

        screen_info = Properties.load_screen_info(resolution)
        if resolution is None:
            with open(self.filename, 'r', encoding='utf-8') as properties:
                for line in properties.readlines():
                    setting, value = separate(line)
                    if "Scale" in setting:
                        self.screen_scale = float(value)
                    else:
                        screen_info = Properties.load_screen_info(value)
        for i, info in enumerate(screen_info):
            self.screen[i] = info

    def save_file(self) -> None:
        with open(self.filename, 'w', encoding='utf-8') as properties:
            properties.write(
                "# Refers to the main screen which the game is located\n")
            properties.write(f"screenScale={self.screen_scale}\n")
            properties.write("screenResolution=1280x800\n")

    @staticmethod
    def load_screen_info(resolution: str) -> List[int]:
        """Returns a tuple containing (screenX, screenY, screenWidth, screenHeight)."""
        if resolution == '800x600':
            return (370, 525, 75, 75)
        if resolution == '1280x800':
            return (600, 699, 95, 95)
        # Catch all
        return (0, 0, 1920, 1080)


properties = Properties()
properties.load_file()
