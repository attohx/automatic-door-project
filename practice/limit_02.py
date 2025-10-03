"""
This script monitors a limit switch connected to a Raspberry Pi GPIO pin.
"""


import RPi.GPIO as GPIO
from time import sleep

# Set the GPIO mode to BOARD
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pin for your button
SWITCH_PIN = 36

# Define debounce time in milliseconds
DEBOUNCE_TIME_MS = 200  # 200 milliseconds

# Set the initial state and pull-up resistor for the button
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the button state and previous state
switch_state = GPIO.input(SWITCH_PIN)
prev_switch_state = switch_state

# Define a function to handle button presses
def button_callback(channel):
    global switch_state
    switch_state = GPIO.input(SWITCH_PIN)

# Add an event listener for the button press
GPIO.add_event_detect(SWITCH_PIN, GPIO.BOTH, callback=button_callback, bouncetime=DEBOUNCE_TIME_MS)

try:
    # Main loop
    while True:
        # Check if the button state has changed
        if switch_state != prev_switch_state:
            if switch_state == GPIO.HIGH:
                #print("The limit switch: TOUCHED -> UNTOUCHED")
                print("The door has been opened")

            else:
                #print("The limit switch: UNTOUCHED -> TOUCHED")
                print("The door has been closed")
            
            prev_switch_state = switch_state


        if switch_state == GPIO.HIGH:
            #print("The limit switch: UNTOUCHED")
            print("The door is open")
        else:
            #print("The limit switch: TOUCHED")
            print("The door is closed")

        sleep(1)


except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()

