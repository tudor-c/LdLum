import random
import time
import copy
from dataclasses import dataclass
from grid import activateLine, Color

@dataclass
class Point:
    x: int
    y: int

class Game:
    _LEVELS = [
        """ .x..x.x.
            .xx.x...
            .....x.x
            .x.x.x.x
            ...x.... """,
    ]
    _HEIGHT = 5
    _WIDTH = 8

    def __init__(self):
        self.level = Game.convert_level_to_data(random.choice(Game._LEVELS).splitlines())
        self.player = Point(0, 0)
        self.enemy = Point(Game._WIDTH - 1, Game._HEIGHT - 1)

    def _print_level(self):
        display = copy.deepcopy(self.level)
        display[self.player.y][self.player.x] = Color.BOTH
        for i in range(Game._HEIGHT):
            activateLine(i, display[i])
            time.sleep(0.001)

    @staticmethod
    def convert_level_to_data(level: str) -> list[list[Color]]:
        return [
            [Color.OFF if c == '.' else Color.GREEN for c in line.strip()] for line in level
        ]

    def start(self):
        while True:
            self._print_level()








