import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.OUT)
try:
    while True:
        GPIO.output(24, GPIO.HIGH)  # Turn on
        time.sleep(1)               # Wait for 1 second
        GPIO.output(24, GPIO.LOW)   # Turn off
        time.sleep(1)                # Wait for 1 second
except KeyboardInterrupt:
    GPIO.cleanup()                 # Clean up on exit
