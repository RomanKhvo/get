import RPi.GPIO as gp


def dtb(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]



dac = [26,19,13,6,5,11,9,10]

gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)

prov=0

try:
    while True and prov ==0:
        z =(input('Число: '))
        if z =='q':
            prov = 1
        else:
            try:
                if int(float(z))-float(z)!=0:
                    print('ввод не целого числа')
                elif float(z)<0:
                    print('ввод отрицательного значения')
                elif float(z)>255:
                    print('ввод значения превышающего возможности 8-разрядного ЦАП')
                else:
                    gp.output(dac,dtb(int(float(z))))
                    print(f'{int(float(z))*3.3/256:.3} Вольт')
            except:
                print('ввод не числового значения')        

finally:
    gp.output(dac,0)
    gp.cleanup()