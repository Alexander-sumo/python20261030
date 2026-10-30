from gpiozero import LED
from time import sleep

led = LED(17)

def flash(duration):
    led.on()
    sleep(duration)
    led.off()
    sleep(0.2)

# Three short
for n in range(3):
    flash(0.2)

# Three long
for n in range(3):
    flash(0.6)

# Three short
for n in range(3):
    flash(0.2)

sleep(1)
