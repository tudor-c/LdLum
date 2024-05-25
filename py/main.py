#!/bin/python3
import RPi.GPIO as GPIO
import shift_register as SR
import time

GPIO.setmode(GPIO.BOARD)

def main():
    print("Labirint din LED-uri - proiect SI")

    while True:
        temp = 1
        for i in range(0, 8):
            SR.writeOut(temp)
            temp <<= 1
            time.sleep(0.2)

        for i in range(0, 8):
            temp >>= 1
            SR.writeOut(temp)
            time.sleep(0.2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\ndone")
