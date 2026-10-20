#Voglio controllare la temperatura esterna con PyPico
#utilizzo il software Thonny su KDE Neon

from machine import ADC
from utime import sleep

sensor = ADC(4)
step = 0

while True:
    voltage = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (voltage - 0.706) / 0.001721

    slep +=1
    
    print(f"{step} - {temperature}")    
    sleep(1)

