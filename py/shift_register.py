#!/bin/python3

import RPi.GPIO as GPIO
# import time

LATCH = 11
CLK = 12
DATA_BIT = 7

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LATCH, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DATA_BIT, GPIO.OUT)

GPIO.output(LATCH, 0)
GPIO.output(CLK, 0)

def _shiftRegister():
    GPIO.output(CLK, 1)
    # time.sleep(0.001)
    GPIO.output(CLK, 0)

def _updateLatch():
    GPIO.output(LATCH, 1)
    # time.sleep(0.001)
    GPIO.output(LATCH, 0)

def writeOut(value):
    for x in range(0, 8):
        temp = value & 0x80
        if temp == 0x80:
            GPIO.output(DATA_BIT, 1)
        else:
            GPIO.output(DATA_BIT, 0)
        _shiftRegister()
        value <<= 1
    _updateLatch()