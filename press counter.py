from gpiozero import Button
from signal import pause

count = 0

def hello():
    global count
    count += 1
    print(f"pressed! Total presses: {count}")

button = Button(27, bounce_time=0.05)
button.when_pressed = hello      # the function itself, no parentheses

pause()                           # sleep forever; events do the work
