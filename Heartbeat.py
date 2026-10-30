from gpiozero import LED
from time import sleep

led = LED(17)          # BCM number: GPIO17, physical pin 11

tempo = 1.0            # Controls the heartbeat speed

while True:
    led.on()
    sleep(0.2)         # Short ON

    led.off()
    sleep(tempo)       # Long OFF
