#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)

try:
    count = 0
    while True:
            print(count)
            count += 1
            GPIO.output(8, GPIO.HIGH)

            sleep(1)

            GPIO.output(8, GPIO.LOW)

            sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print()
