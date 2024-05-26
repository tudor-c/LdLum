from enum import Enum
from RPi import GPIO
from shift_register import SN74HC595

_shift_reg1 = SN74HC595(latch_clk=11, shift_clk=12, data_bit=13)
_shift_reg2 = SN74HC595(latch_clk=15, shift_clk=16, data_bit=18)

GPIO.setmode(GPIO.BOARD)
LINES_PINS = [19, 21, 22, 23, 24]
for pin in LINES_PINS:
    GPIO.setup(pin, GPIO.OUT)


class Color(Enum):
    OFF = "00"
    RED = "01"
    GREEN = "10"
    BOTH = "11"


def activateLine(line: int, cols: list[Color]):
    """
    Activeaza pixelii de pe linia `line` si coloanele din `cols`
    :param x: line in [0, 5)
    :param cols: lista cu 8 elemente cu starea fiecarei coloane de la stanga la dreapta
    """
    state = list(map(lambda v: v.value, cols))
    state.reverse()
    value = int(''.join(state), 2)

    for i in range(5):
        GPIO.output(LINES_PINS[i], GPIO.LOW)

    _shift_reg1.writeOut(value % 256)
    _shift_reg2.writeOut(int(value / 256))

    GPIO.output(LINES_PINS[line], GPIO.HIGH)




