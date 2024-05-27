#!/bin/python3
import traceback
import RPi.GPIO as GPIO
from game import Game

def main():
    print("Labirint din LED-uri - proiect SI")
    Game().start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\ndone")
        GPIO.cleanup()
    except Exception:
        print(traceback.format_exc())
        GPIO.cleanup()
