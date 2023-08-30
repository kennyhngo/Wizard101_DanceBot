from typing import List


def separate(string: str, delimiter="=") -> List[str]:
    """Splits the string into 2 parts based on the separater symbol."""
    idx = string.find(delimiter)
    return [
        string[:idx if idx != -1 else len(string)],
        string[idx+1:] if idx != -1 else ""
    ]


class Globals:
    """For whole program to share a common variable."""
    q_pressed = False
    game_finished = False
