from gpiozero import Button, LED
from signal import pause

button = Button(27, bounce_time=0.05)
led = LED(17)

# LED lights while the button is held
button.when_pressed = led.on
button.when_released = led.off

pause()
