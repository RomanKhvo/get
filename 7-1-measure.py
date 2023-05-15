import RPi.GPIO as gp
import time
from matplotlib import pyplot as plt

gp.setmode(gp.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
gp.setup(leds, gp.OUT)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
gp.setup(dac, gp.OUT, initial=gp.LOW)

comp = 4
troyka = 17
gp.setup(troyka, gp.OUT, initial = gp.LOW)
gp.setup(comp, gp.IN)


def adc():
    k = 0
    for i in range(7, -1, -1):
        k+=2**i
        gp.output(dac, perev(k))
        time.sleep(0.005)
        if gp.input(comp)==0:
            k-=2**i
    return k
    

def perev(a):
    return([int(elem) for elem in bin(a)[2:].zfill(8)])


try:
    napr = 0
    result_ismer = []
    time_start = time.time()
    count = 0
    gp.output(troyka, 0)
    print('Зарядка')
    napr_nach = adc()
    while napr<150:
        napr = adc()
        print(f'{napr} +')
        result_ismer.append(napr)
        time.sleep(0.001)
        count+=1
        gp.output(leds, perev(napr))
    
    gp.output(troyka, 1)

    print('Разрядка')
    while time.time()-time_start<30:
        napr = adc()
        print(f'{napr} -')
        result_ismer.append(napr)
        time.sleep(0.001)
        count+=1
        gp.output(leds, perev(napr))
        print(napr)

    time_experiment = time.time() - time_start

    print("Запись")

    with open('data.txt', 'w') as f:
        for i in result_ismer:
            f.write(str(i) + '\n')
    print(1)
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_experiment/count) + '\n')
        f.write('0.01289')

    print(f'Время: {time_experiment}')
    print('График')
    y = [i/256*3.3 for i in result_ismer]
    x = [i*time_experiment/count for i in range(len(result_ismer))]
    
    plt.plot(x,y)
    plt.xlabel('t, с')
    plt.ylabel('U, В')
    plt.show()


except KeyboardInterrupt():
    gp.output(leds, 0)
    gp.output(dac, 0)
    gp.cleanup()

finally:
    gp.output(leds, 0)
    gp.output(dac, 0)
    gp.cleanup()

