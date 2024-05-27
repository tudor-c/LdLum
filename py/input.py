import time
from enum import Enum
from RPi import GPIO

class Buttons(Enum):
    LEFT    = 26
    DOWN  = 29
    UP  = 31
    RIGHT = 32
    ENTER = 33

_button_states = {}
_last_press_time = {}

MINIMUM_PRESS_TIME_DELTA = 0.4  # delta intre apasari cu rol de debouncer

GPIO.setmode(GPIO.BOARD)
for pin in Buttons:
    GPIO.setup(pin.value, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def isPressed(pin: Buttons) -> bool:
    pin = pin.value
    previously_pressed = _button_states.setdefault(pin, False)
    previous_timestamp = _last_press_time.setdefault(pin, time.time() - 1)
    currently_pressed = GPIO.input(pin) == GPIO.HIGH

    pressed = False
    if (currently_pressed and not previously_pressed and
            time.time() - previous_timestamp >= MINIMUM_PRESS_TIME_DELTA):
        pressed = True
        _last_press_time[pin] = time.time()

    _button_states[pin] = currently_pressed

    return pressed



