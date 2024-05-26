#!/bin/python3
import RPi.GPIO as GPIO
from game import Game

def main():
    print("Labirint din LED-uri - proiect SI")

    # colors = [Color.OFF, Color.BOTH, Color.GREEN, Color.RED, Color.RED, Color.GREEN, Color.GREEN, Color.BOTH]
    # colors = [Color.BOTH] * 8

    game = Game()
    game.start()

    # shift_reg1.writeOut(255)
    # shift_reg2.writeOut(255)
    # GPIO.setup(19, GPIO.OUT)
    # GPIO.setup(21, GPIO.OUT)
    # GPIO.setup(22, GPIO.OUT)
    # GPIO.setup(23, GPIO.OUT)
    # GPIO.setup(24, GPIO.OUT)
    # vals = [19, 21, 22, 23, 24]

    # while True:
    #     for i in range(5):
    #         GPIO.output(vals[i], GPIO.HIGH)
    #         time.sleep(0.2)
    #         GPIO.output(vals[i], GPIO.LOW)
    #         time.sleep(0.2)
    # while True:
    #     temp = 1
    #     for i in range(0, 16):
    #         print(i)
    #         if i < 8:
    #             shift_reg1.writeOut(temp)
    #             shift_reg2.writeOut(0)
    #         else:
    #             shift_reg1.writeOut(0)
    #             shift_reg2.writeOut(temp)
    #         temp <<= 1
    #         if temp > 255:
    #             temp = 1
    #         time.sleep(0.2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\ndone")
