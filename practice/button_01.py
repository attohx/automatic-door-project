from gpiozero import Button
from signal import pause
from time import sleep

button = Button(21)

def when_not_pressed():
    print("Button Not Pressed")
    sleep(1)

def pressed():
    print("Button Pressed")
    sleep(1)

button.when_pressed = pressed
button.when_released = when_not_pressed

pause()