import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)  # Change this pin to an available one

GPIO.output(32, GPIO.HIGH)  # Turn on the pin
print("Pin 32 is on")
GPIO.cleanup()
