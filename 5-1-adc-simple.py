import RPi.GPIO as gp
import time

def dtb(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]

def ya(a):
    signal = dtb(a)
    gp.output(dac,signal)
    return signal


dac = [26,19,13,6,5,11,9,10]
troyka  = 17
comp = 4
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT, initial = gp.LOW)
gp.setup(troyka, gp.OUT, initial = gp.HIGH)
gp.setup(comp, gp.IN)
prov=0

def adc():
    while True:
        for i in range(256):
            signal = ya(i)
            time.sleep(0.01 )
            cv = gp.input(comp)
            vol = i/256 * 3.3
            if cv == 0:
                print(f'{vol:.3} Вольт, {i}')
                break    

try:
    adc()
    
except KeyboardInterrupt:
    pass
finally:
    gp.output(dac,0)
    gp.cleanup()
