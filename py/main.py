#!/bin/python3
import RPi.GPIO as GPIO
from shift_register import SN74HC595
import time


def main():
    print("Labirint din LED-uri - proiect SI")

    GPIO.setmode(GPIO.BOARD)

    shift_reg1 = SN74HC595(latch_clk=11, shift_clk=12, data_bit=13)
    shift_reg2 = SN74HC595(latch_clk=15, shift_clk=16, data_bit=18)

    while True:
        temp = 1
        for i in range(0, 16):
            print(i)
            if i < 8:
                shift_reg1.writeOut(temp)
                shift_reg2.writeOut(0)
            else:
                shift_reg1.writeOut(0)
                shift_reg2.writeOut(temp)
            temp <<= 1
            if temp > 255:
                temp = 1
            time.sleep(0.2)

        # for i in range(0, 8):
        #     temp >>= 1
        #     shift_reg1.writeOut(temp)
        #     time.sleep(0.2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\ndone")
