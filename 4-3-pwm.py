import RPi.GPIO as gp
dac = [26,19,13,6,5,11,9,10]
gp.setmode(gp.BCM)
gp.setup(22,gp.OUT)
gp.setup(24,gp.OUT)

t = 0
pr = gp.PWM(22,1000)
pr.start(0)

led = gp.PWM(24,1000)
led.start(0)


try:
    while True:
        t = int(input())
        pr.ChangeDutyCycle(t)
        led.ChangeDutyCycle(t)


finally:
    gp.output(dac,0)
    gp.cleanup()