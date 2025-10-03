import RPi.GPIO as GPIO
from time import sleep

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pin for your button
SWITCH_PIN = 36  # Change this to the pin you are using

# Set up the pin as an input with a pull-up resistor
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    while True:
        if GPIO.input(SWITCH_PIN) == GPIO.LOW:
            print("The door is closed")
        else:
            print("The door is open")

        sleep(1)


except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()
    print("\n")
