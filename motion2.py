from gpiozero import MotionSensor
from signal import pause
from servo2 import handleServo
import time
from datetime import datetime
import RPi.GPIO as GPIO

# Initialize the motion sensor on GPIO pin 23
pir = MotionSensor(23)

# Global variables
MANUAL_MODE = True
#LAST_MOTION_TIME = None

def movementDetected():
    global MANUAL_MODE
    global LAST_MOTION_TIME
    if MANUAL_MODE:
        handleServo("open")
        time.sleep(2)
        handleServo("close")
        time.sleep(2)
       # LAST_MOTION_TIME = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

try:
    while True:
        pir.wait_for_motion()
        print("Movement detected")
        # LAST_MOTION_TIME = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        movementDetected()
        pir.wait_for_no_motion()

except KeyboardInterrupt:
    print("Program stopped")
    GPIO.cleanup()