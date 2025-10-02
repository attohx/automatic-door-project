from gpiozero import LED, Button
from signal import pause

led = LED(12)
button = Button(21)

# def press_button():
#     if led.is_lit:
#         led.off()
#     else:
#         led.on()

# button.when_pressed = press_button

global led_on
led_on = False
def press_button():
    global led_on
    if led_on:
        led.off()
        led_on = False
    else:
        led.on()
        led_on = True

button.when_pressed = press_button

pause()