import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin 11 as an output, and define as servo1 as PWM pin
GPIO.setup(18,GPIO.OUT)
servo1 = GPIO.PWM(18,50) # pin 11 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)

angle1 = 0.0
angle2 = 180.0


def handleServo(status):
    if status == "open":
        servo1.ChangeDutyCycle(2+(angle1/18))
    elif status == "close":
        servo1.ChangeDutyCycle((angle2/18)-1)

    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)