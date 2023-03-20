import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
dac = [26,19,13,6,5,11,9,10]

gp.setup(dac, gp.OUT)


def dtb(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]



try:
    t = int(input())
    for i in range(0,256):
        gp.output(dac,dtb(i))
        time.sleep(t/256/2)
    for i in range(255,-1,-1):
        gp.output(dac,dtb(i))
        time.sleep(t/256/2)

finally:
    gp.output(dac, 0)
    gp.cleanup()