import random
import time
from grid import activateLine, Color

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

    def _print_level(self):
        for i in range(Game._HEIGHT):
            activateLine(i, self.level[i])
            time.sleep(0.001)

    @staticmethod
    def convert_level_to_data(level: str) -> list[list[Color]]:
        return [
            [Color.OFF if c == '.' else Color.GREEN for c in line.strip()] for line in level
        ]

    def start(self):
        print(self.level)
        while True:
            self._print_level()








