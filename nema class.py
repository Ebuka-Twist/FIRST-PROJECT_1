from machine import Pin
import time

class DRV8825StepperDriver:
    def __init__(self, step_pin, dir_pin, enable_pin, steps_per_rev=200):
        self.step = Pin(step_pin, Pin.OUT)
        self.dir = Pin(dir_pin, Pin.OUT)
        self.enable = Pin(enable_pin, Pin.OUT)
        self.steps_per_rev = steps_per_rev

    def enable_motor(self):
        self.enable.value(0)  # Set enable pin low to enable the motor

    def disable_motor(self):
        self.enable.value(1)  # Set enable pin high to disable the motor

    def rotate_degrees(self, degrees, direction="clockwise"):
        steps = int(self.steps_per_rev * degrees / 360)
        self.rotate_steps(steps, direction)

    def rotate_steps(self, steps, direction="clockwise"):
        self.enable_motor()  # Enable the motor
        self.dir.value(1 if direction == "clockwise" else 0)
        for _ in range(steps):
            self.step.value(1)
            time.sleep_us(500)  # Adjust delay as needed
            self.step.value(0)
            time.sleep_us(2000)  # Adjust delay as needed
        self.disable_motor()  # Disable the motor after rotation

# Example usage:
stepper = DRV8825StepperDriver(step_pin=13, dir_pin=14, enable_pin=15)  # Adjust pin numbers
for i in range(100):
    
# Rotate 90 degrees clockwise
    stepper.rotate_degrees(degrees=180, direction="clockwise")
    time.sleep(0.3)  # Wait for motor to stop

# Rotate 45 degrees counterclockwise
    stepper.rotate_degrees(degrees=180, direction="counterclockwise")
    time.sleep(0.1)  # Wait for motor to stop
