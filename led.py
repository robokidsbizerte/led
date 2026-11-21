from gpiozero import LED
from time import sleep

led = LED(18)

print("Test LED sur GPIO 17 (Pin 11)... Ctrl+C pour arrêter.")

while True:
    led.on()
    print("LED ALLUMÉE")
    sleep(0.5)
    led.off()
    print("LED ÉTEINTE")
    sleep(0.5)