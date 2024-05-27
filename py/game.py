import random
import time
import copy
from bdfparser import Font
from dataclasses import dataclass
from grid import activateLine, Color, convertDataToGrid
from input import Buttons, isPressed


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Game:
    _LEVELS = [
        """ .x..x..x
            .xx.xx..
            .....x.x
            .x.x...x
            ...x.x.. """,

        """ ....x...
            .xx.x.x.
            ..x...x.
            x...x.x.
            ..x..... """,

        """ ........
            xxxxx.x.
            ........
            .xxxxx.x
            ........ """,

        """ .xx.....
            ....x.x.
            x.xxx.x.
            x.x.xxx.
            x....... """,
    ]
    _HEIGHT = 5
    _WIDTH = 8
    _FONT = Font('res/spleentt-5x8-font/SpleenttMedium-8.bdf')

    def __init__(self):
        self.level = None
        self.player_pos = None
        self.enemy_pos = None
        self._init()

    def _init(self):
        level_data = [line.strip() for line in random.choice(Game._LEVELS).splitlines()]
        self.level = convertDataToGrid(level_data, Color.GREEN)
        self.player_pos = Point(0, 0)
        self.enemy_pos = Point(Game._WIDTH - 1, Game._HEIGHT - 1)

    def _isValid(self, pos: Point) -> bool:
        if (pos.x >= 0 and pos.y >= 0 and pos.x < Game._WIDTH and pos.y < Game._HEIGHT and
                self.level[pos.y][pos.x] == Color.OFF):
            return True
        return False

    def _printGrid(self, grid, print_players: bool):
        display = copy.deepcopy(grid)

        if print_players:
            display[self.player_pos.y][self.player_pos.x] = Color.ALL
            if int(time.time() * 10) % 7 != 0:
                display[self.enemy_pos.y][self.enemy_pos.x] = Color.RED

        for i in range(Game._HEIGHT):
            activateLine(i, display[i])
            time.sleep(0.001)

    def _printLetter(self, letter: str, color: Color, duration: float):
        glyph = str(Game._FONT.glyph(letter).draw()).splitlines()
        glyph = [[glyph[i][j] for i in range(len(glyph))]
                    for j in reversed(range(len(glyph[0])))]
        letter = convertDataToGrid(glyph, color)

        start = time.time()
        while time.time() - start < duration:
            self._printGrid(letter, False)

    def _printText(self, text: str, color: Color = Color.ALL, letter_duration: float =0.4):
        for c in text:
            self._printLetter(c, color, letter_duration)
        self._clearScreen()

    def _clearScreen(self):
        clear_grid = [[Color.OFF for _ in range(Game._WIDTH)] for _ in range(Game._HEIGHT)]
        self._printGrid(clear_grid, False)

    def _movePlayer(self) -> bool:
        """
        Citeste input-ul de la butoane si muta jucatorul in caz de apasare.

        :return: True if player moved, Flase otherwise
        """
        x = self.player_pos.x
        y = self.player_pos.y

        if isPressed(Buttons.LEFT):
            new_pos = Point(x - 1, y)
            if self._isValid(new_pos):
                self.player_pos = new_pos
                return True
        if isPressed(Buttons.RIGHT):
            new_pos = Point(x + 1, y)
            if self._isValid(new_pos):
                self.player_pos = new_pos
                return True
        if isPressed(Buttons.UP):
            new_pos = Point(x, y - 1)
            if self._isValid(new_pos):
                self.player_pos = new_pos
                return True
        if isPressed(Buttons.DOWN):
            new_pos = Point(x, y + 1)
            if self._isValid(new_pos):
                self.player_pos = new_pos
                return True
        return False

    def _moveEnemy(self):
        dirs = [
            Point(-1, 0),  # left
            Point(0, -1),  #up
            Point(1, 0),  # right
            Point(0, 1),  # down
        ]
        random.shuffle(dirs)
        for direction in dirs:
            new_pos = self.enemy_pos + direction
            if self._isValid(new_pos):
                self.enemy_pos = new_pos
                break

    def _playerLost(self) -> bool:
        if self.player_pos == self.enemy_pos:
            return True
        elif (abs(self.player_pos.x - self.enemy_pos.x) +
              abs(self.player_pos.y - self.enemy_pos.y) == 0):
            return True
        return False

    def _playerWon(self) -> bool:
        if (self.player_pos == Point(Game._WIDTH - 1, Game._HEIGHT - 1) and
            self.player_pos != self.enemy_pos):
            return True
        return False

    def _checkRestart(self):
        """
        Reporneste jocul daca se apasa tasta ENTER
        """
        if isPressed(Buttons.ENTER):
            self._clearScreen()
            self.start()

    def start(self):
        time.sleep(1)
        self._init()
        self._printText("START")
        while True:
            self._checkRestart()
            moved = self._movePlayer()

            if self._playerWon():
                self._clearScreen()
                time.sleep(1)
                self._printText("AI CASTIGAT")
                time.sleep(1)
                self.start()

            if self._playerLost():
                self._clearScreen()
                time.sleep(1)
                self._printText("AI PIERDUT")
                time.sleep(1)
                self.start()

            if moved:
                self._moveEnemy()

            self._printGrid(self.level, True)









