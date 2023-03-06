import time
import RPi.GPIO as gp

a = [22,23,27,18,15,14,3,2]
gp.setmode(gp.BCM)
gp.setup(a,gp.IN)

while True:
    time.sleep(1)
    for i in range(8):
        print(gp.input(a[i]),end = ' ')
    print()
