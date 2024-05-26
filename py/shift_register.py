#!/bin/python3

import RPi.GPIO as GPIO
import time

# LATCH = 11
# CLK = 12
# DATA_BIT = 7


class SN74HC595:
    def __init__(self, latch_clk, shift_clk, data_bit):
        self.latch_clk = latch_clk
        self.shift_clk = shift_clk
        self.data_bit = data_bit

        GPIO.setup(self.latch_clk, GPIO.OUT)
        GPIO.setup(self.shift_clk, GPIO.OUT)
        GPIO.setup(self.data_bit, GPIO.OUT)

        GPIO.output(self.latch_clk, 0)
        GPIO.output(self.shift_clk, 0)

    def _shiftRegister(self):
        GPIO.output(self.shift_clk, 1)
        time.sleep(0.001)
        GPIO.output(self.shift_clk, 0)

    def _updateLatch(self):
        GPIO.output(self.latch_clk, 1)
        time.sleep(0.001)
        GPIO.output(self.latch_clk, 0)

    def writeOut(self, value):
        for x in range(0, 8):
            temp = value & 0x80
            if temp == 0x80:
                GPIO.output(self.data_bit, 1)
            else:
                GPIO.output(self.data_bit, 0)
            self._shiftRegister()
            value <<= 1
        self._updateLatch()