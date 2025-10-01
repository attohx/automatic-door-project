# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
pwm = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
pwm.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)

def set_servo_angle(angle):
    duty_cycle = (angle / 18) + 2.5
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Give the servo time to reach the desired angle

# set_servo_angle(0)

# for angle in range(0, 181, 10):
#             set_servo_angle(angle)

try:
    while True:
        # Rotate the servo from 0 to 180 degrees
        for angle in range(0, 181, 90):
            set_servo_angle(angle)

        # Rotate the servo back from 180 to 0 degrees
        for angle in range(180, -1, -90):
            set_servo_angle(angle)

except KeyboardInterrupt:
    # If the user presses Ctrl+C, clean up the GPIO configuration
    set_servo_angle(0)
    pwm.stop()
    GPIO.cleanup()
    print ("\nGoodbye")

# pwm.stop()
# GPIO.cleanup()
# print ("\nGoodbye")