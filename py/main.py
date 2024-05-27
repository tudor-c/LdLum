#!/bin/python3
import RPi.GPIO as GPIO
from game import Game

def main():
    print("Labirint din LED-uri - proiect SI")

    game = Game()
    game.start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\ndone")
        GPIO.cleanup()
    except Exception as e:
        print(e)
        GPIO.cleanup()
