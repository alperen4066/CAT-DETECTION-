from gpiozero import Servo
from time import sleep

# Configure the Servo on GPIO 18 with specific pulse width values for 0 and 180 degrees
servo = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

def turn_servo(angle):
    # Convert angle to a value between -1 and 1
    value = (angle / 180.0) * 2 - 1
    servo.value = value
    print(f"Servo turned to {angle} degrees")

try:
    while True:
        # Turn to 0 degrees
        turn_servo(0)
        sleep(2)  # Wait for 2 seconds
        
        # Turn to 180 degrees
        turn_servo(180)
        sleep(2)  # Wait for 2 seconds
        
except KeyboardInterrupt:
    print("Program stopped")
