# Import libraries
import RPi.GPIO as GPIO
import time

class Door():
    def __init__(self, servo_pin):
        self.servo_pin = servo_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.servo_pin, 50)  # 50Hz pulse
        time.sleep(2)  # Allow time for the servo to initialize

    def set_angle(self, angle):
        duty_cycle = (angle / 18) + 2.5
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5)  # Give the servo time to reach the desired angle

    def open(self):
        self.pwm.start(0)
        self.set_angle(90)  # Open position
        print("Door is open")
        self.pwm.stop()

    def close(self):
        self.pwm.start(0)
        self.set_angle(0)   # Closed position
        print("Door is closed")   
        self.pwm.stop()

    def cleanup(self):
        GPIO.cleanup()