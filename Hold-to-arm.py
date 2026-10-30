from gpiozero import Button, LED
from signal import pause

button = Button(27, bounce_time=0.05)
led = LED(17)

# Inverted: LED is ON until the button is pressed
led.on()

button.when_pressed = led.off
button.when_released = led.on

pause()
