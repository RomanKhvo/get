import RPi.GPIO as gpio

import time

gpio.setmode(gpio.BCM)
gpio.setup(14,gpio.IN)
gpio.setup(23,gpio.OUT)


while True:
    gpio.output(23,gpio.input(14))







