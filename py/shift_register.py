#!/bin/python3

import RPi.GPIO as GPIO

class SN74HC595:
    def __init__(self, latch_clk, shift_clk, data_bit):
        self._latch_clk = latch_clk
        self._shift_clk = shift_clk
        self._data_bit = data_bit

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self._latch_clk, GPIO.OUT)
        GPIO.setup(self._shift_clk, GPIO.OUT)
        GPIO.setup(self._data_bit, GPIO.OUT)

        GPIO.output(self._latch_clk, 0)
        GPIO.output(self._shift_clk, 0)
        self.writeOut(0)

    def _shiftRegister(self):
        GPIO.output(self._shift_clk, 1)
        GPIO.output(self._shift_clk, 0)

    def _updateLatch(self):
        GPIO.output(self._latch_clk, 1)
        GPIO.output(self._latch_clk, 0)

    def writeOut(self, value):
        for x in range(0, 8):
            temp = value & 0x80
            if temp == 0x80:
                GPIO.output(self._data_bit, 1)
            else:
                GPIO.output(self._data_bit, 0)
            self._shiftRegister()
            value <<= 1
        self._updateLatch()