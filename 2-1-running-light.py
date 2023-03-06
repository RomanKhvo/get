import RPi.GPIO as GP
import time
leds = [21,20,16,12,7,8,25,24]
GP.setmode(GP.BCM)
GP.setup(leds, GP.OUT)
for i in range(3):
    for i in range(8):
        GP.output(leds[i],1)
        time.sleep(0.2)
        GP.output(leds[i],0)
GP.output(leds,0)
GP.cleanup()
