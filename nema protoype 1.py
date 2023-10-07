import machine
import time

# Define the GPIO pins connected to the DRV8825 driver
STEP_PIN = machine.Pin(13, machine.Pin.OUT)
DIR_PIN = machine.Pin(14, machine.Pin.OUT)
ENABLE_PIN = machine.Pin(15, machine.Pin.OUT)
delay =0.001
# Define the number of steps per revolution for your stepper motor
STEPS_PER_REV = 200  # Change this value based on your motor's specification
#delay =0.01
# Function to enable the stepper motor
def enable_stepper():
    ENABLE_PIN.value(0)

# Function to disable the stepper motor
def disable_stepper():
    ENABLE_PIN.value(1)

# Function to rotate the stepper motor clockwise
def rotate_clockwise(angle):
    enable_stepper()
    
    # Calculate the number of steps needed to rotate the desired angle
    steps = int((angle / 360) * STEPS_PER_REV)
    
    # Set the direction (clockwise)
    DIR_PIN.value(1)
    
    # Generate pulses to step the motor
    for _ in range(steps):
        STEP_PIN.value(1)
        time.sleep_us(500)
        STEP_PIN.value(0)
        time.sleep_us(2000)
    
    disable_stepper()

# Function to rotate the stepper motor counterclockwise
def rotate_counterclockwise(angle):
    enable_stepper()
    
    # Calculate the number of steps needed to rotate the desired angle
    steps = int((angle / 360) * STEPS_PER_REV)
    
    # Set the direction (counterclockwise)
    DIR_PIN.value(0)
    
    # Generate pulses to step the motor
    for _ in range(steps):
        STEP_PIN.value(1)
        time.sleep_us(500)
        STEP_PIN.value(0)
        time.sleep_us(2000)
    
    disable_stepper()


# Example usage:
# Rotate the motor 90 degrees clockwise with a 2ms delay between steps
for i in range(100):
    
    
    rotate_clockwise(180)
    time.sleep(0.1)
# Rotate the motor 180 degrees counterclockwise with a 2ms delay between steps
    rotate_counterclockwise(180)
    time.sleep(0.1)
    #rotate_clockwise(145)
    #time.sleep(0.4)
    #rotate_counterclockwise(120, delay_ms=5)
    #utime.sleep(2)


