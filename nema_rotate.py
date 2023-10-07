import machine
import utime

# Define the GPIO pins connected to the DRV8825 driver
STEP_PIN = machine.Pin(0, machine.Pin.OUT)
DIR_PIN = machine.Pin(1, machine.Pin.OUT)
ENABLE_PIN = machine.Pin(2, machine.Pin.OUT)

# Define the number of steps per revolution for your stepper motor
STEPS_PER_REV = 200  # Change this value based on your motor's specification

# Function to enable the stepper motor
def enable_stepper():
    ENABLE_PIN.value(0)

# Function to disable the stepper motor
def disable_stepper():
    ENABLE_PIN.value(1)

# Function to rotate the stepper motor clockwise
def rotate_clockwise(angle, delay_ms=2):
    enable_stepper()
    
    # Calculate the number of steps needed to rotate the desired angle
    steps = int((angle / 360) * STEPS_PER_REV)
    
    # Set the direction (clockwise)
    DIR_PIN.value(1)
    
    # Generate pulses to step the motor
    for _ in range(steps):
        STEP_PIN.value(1)
        utime.sleep_ms(delay_ms)
        STEP_PIN.value(0)
        utime.sleep_ms(delay_ms)
    
    disable_stepper()

# Function to rotate the stepper motor counterclockwise
def rotate_counterclockwise(angle, delay_ms=2):
    enable_stepper()
    
    # Calculate the number of steps needed to rotate the desired angle
    steps = int((angle / 360) * STEPS_PER_REV)
    
    # Set the direction (counterclockwise)
    DIR_PIN.value(0)
    
    # Generate pulses to step the motor
    for _ in range(steps):
        STEP_PIN.value(1)
        utime.sleep_ms(delay_ms)
        STEP_PIN.value(0)
        utime.sleep_ms(delay_ms)
    
    disable_stepper()

# Example usage:
# Rotate the motor 90 degrees clockwise with a 2ms delay between steps
for i in range(100):
    
    #rotate_clockwise(0, delay_ms=5)
   # utime.sleep(3)
    rotate_clockwise(90, delay_ms=3)
    utime.sleep(0.04)
# Rotate the motor 180 degrees counterclockwise with a 2ms delay between steps
    rotate_counterclockwise(180, delay_ms=2)
    utime.sleep(0.03)
    rotate_clockwise(90, delay_ms=3)
    utime.sleep(0.08)
    rotate_clockwise(0, delay_ms=2)
    utime.sleep(0.06)
    rotate_clockwise(120, delay_ms=5)
    utime.sleep(0.04)
