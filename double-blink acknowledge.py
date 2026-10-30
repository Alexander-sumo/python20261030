from gpiozero import Button, LED
from signal import pause
from time import sleep

button = Button(27, bounce_time=0.05)
led = LED(17)

def acknowledge():
    previous_state = led.is_lit

    for n in range(2):
        led.on()
        sleep(0.15)
        led.off()
        sleep(0.15)

    if previous_state:
        led.on()
    else:
        led.off()

button.when_pressed = acknowledge

pause()
