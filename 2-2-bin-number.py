import RPi.GPIO as GP
import time
dac = [26,19,13,6,5,11,9,10]
GP.setmode(GP.BCM)
GP.setup(dac, GP.OUT)


x=7


stok = bin(x)[2:]
while len(stok)<8:
    stok ='0'+stok

number = [int(i) for i in stok]
GP.output(dac,number)
time.sleep(5)
GP.output(dac,0)
GP.cleanup()