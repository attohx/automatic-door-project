# Import libraries
import RPi.GPIO as GPIO
from time import sleep


class Door():
    def __init__(self, servo_pin):
        self.servo_pin = servo_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.servo_pin, 50)  # 50Hz pulse
        sleep(2)  # Allow time for the servo to initialize
        self.pwm.start(0)

    def set_angle(self, angle):
        duty_cycle = (angle / 18) + 2.5
        self.pwm.ChangeDutyCycle(duty_cycle)
        sleep(0.5)  # Give the servo time to reach the desired angle
        self.pwm.ChangeDutyCycle(0)  # Stop sending signal to avoid jittering

    def open(self):
        self.set_angle(0)  # Open position
        print("Door is open")
        # self.cleanup()

    def close(self):
        self.set_angle(170)   # Closed position
        print("Door is closed")
        # self.cleanup()

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()
        print("GPIO cleaned up")

if __name__ == "__main__":
    a_door = Door(11)  # Example usage with pin 11
    a_door.open()
    sleep(2)
    a_door.close()
    sleep(2)
    a_door.set_angle(45)  # Set to mid position
    sleep(2)
    a_door.close()
    a_door.cleanup()