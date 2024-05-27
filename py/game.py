import random
import time
import copy
from dataclasses import dataclass
from grid import activateLine, Color, convertGridToData
from input import Buttons, isPressed


@dataclass
class Point:
    x: int
    y: int

class Game:
    _LEVELS = [
        """ .x..x..x
            .xx.xx..
            .....x.x
            .x.x.x.x
            ...x.... """,
    ]
    _HEIGHT = 5
    _WIDTH = 8

    def __init__(self):
        self.level = None
        self.player_pos = None
        self.enemy = None

    def _isValid(self, pos: Point) -> bool:
        if (pos.x >= 0 and pos.y >= 0 and pos.x < Game._WIDTH and pos.y < Game._HEIGHT and
                self.level[pos.y][pos.x] == Color.OFF):
            return True
        return False

    def _init(self):
        self.level = convertGridToData(random.choice(Game._LEVELS).splitlines())
        self.player_pos = Point(0, 0)
        self.enemy = Point(Game._WIDTH - 1, Game._HEIGHT - 1)

    def _printLevel(self):
        display = copy.deepcopy(self.level)
        display[self.player_pos.y][self.player_pos.x] = Color.BOTH
        for i in range(Game._HEIGHT):
            activateLine(i, display[i])
            time.sleep(0.001)

    def _movePlayer(self):
        x = self.player_pos.x
        y = self.player_pos.y

        if isPressed(Buttons.LEFT):
            new_pos = Point(x - 1, y)
            if self._isValid(new_pos):
                self.player_pos = new_pos
        if isPressed(Buttons.RIGHT):
            new_pos = Point(x + 1, y)
            if self._isValid(new_pos):
                self.player_pos = new_pos
        if isPressed(Buttons.UP):
            new_pos = Point(x, y - 1)
            if self._isValid(new_pos):
                self.player_pos = new_pos
        if isPressed(Buttons.DOWN):
            new_pos = Point(x, y + 1)
            if self._isValid(new_pos):
                self.player_pos = new_pos

    def start(self):
        self._init()
        while True:
            if isPressed(Buttons.ENTER):
                # reia jocul
                self.start()
                continue

            self._movePlayer()
            self._printLevel()









