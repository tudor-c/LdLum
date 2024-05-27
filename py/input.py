from enum import Enum
from RPi import GPIO

class Buttons(Enum):
    LEFT    = 26
    DOWN  = 29
    UP  = 31
    RIGHT = 32
    ENTER = 33

_BUTTON_STATES = {}

GPIO.setmode(GPIO.BOARD)
for pin in Buttons:
    GPIO.setup(pin.value, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def isPressed(pin: Buttons) -> bool:
    pin = pin.value
    previously_pressed = _BUTTON_STATES.setdefault(pin, False)
    currently_pressed = GPIO.input(pin) == GPIO.HIGH

    pressed = False
    if currently_pressed and not previously_pressed:
        pressed = True

    _BUTTON_STATES[pin] = currently_pressed
    return pressed


