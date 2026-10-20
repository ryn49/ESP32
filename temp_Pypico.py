#da caricare con Thonny

from machine import ADC, Pin

# Inizializzo l'ADC sul pin 26 (ADC0)
adc = ADC(Pin(26))

# Leggo il valore (0-65535) sul pin di ingresso
valore = adc.read_u16()
print("Valore ADC:", valore)

# converto in tensione (la tensione di lavoro del PyPico 3.3V)
tensione = valore * 3.3 / 65535
print("Tensione (v):", round(tensione, 2))

