from gpiozero import MotionSensor
from signal import pause

# Initialize the motion sensor on GPIO pin 23
pir = MotionSensor(23)

# Define the actions for motion detected and motion ended
def on_motion():
    print("Motion Detected!")

def on_no_motion():
    print("No Motion")

# Attach the actions to the motion sensor
pir.when_motion = on_motion
pir.when_no_motion = on_no_motion

print("PIR Module Test (CTRL+C to exit)")
pause()  # Wait for an interrupt (CTRL+C to exit)
