from machine import Pin
import time
import math
from time import sleep

# MPU6050 registers
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT = 0x3B
ACCEL_YOUT = 0x3D
ACCEL_ZOUT = 0x3F
GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47

# MPU6050 constants
GYRO_SCALE = 131.0
ACCEL_SCALE = 16384.0

# Configure I2C communication

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0),freq=400000)
devices = i2c.scan()

if 0x68 in devices:
    i2c.writeto_mem(0x68, PWR_MGMT_1, bytearray([0x00]))  # Wake up the MPU6050
    i2c.writeto_mem(0x68, SMPLRT_DIV, bytearray([0x07]))  # Set sample rate to 1kHz
    i2c.writeto_mem(0x68, CONFIG, bytearray([0x00]))  # Set digital low-pass filter to 260Hz
    i2c.writeto_mem(0x68, GYRO_CONFIG, bytearray([0x18]))  # Set gyro full-scale range to +/-2000 degrees per second
    i2c.writeto_mem(0x68, INT_ENABLE, bytearray([0x01]))  # Enable data ready interrupt

def read_word_2c(addr):
    high = i2c.readfrom_mem(0x68, addr, 1)
    low = i2c.readfrom_mem(0x68, addr+1, 1)
    value = (high[0] << 8) + low[0]
    if value >= 0x8000:
        return -((65535 - value) + 1)
    else:
        return value

def get_acceleration_data():
    x = read_word_2c(ACCEL_XOUT) / ACCEL_SCALE
    y = read_word_2c(ACCEL_YOUT) / ACCEL_SCALE
    z = read_word_2c(ACCEL_ZOUT) / ACCEL_SCALE
    return x, y, z

def get_rotation_data():
    x = read_word_2c(GYRO_XOUT) / GYRO_SCALE
    y = read_word_2c(GYRO_YOUT) / GYRO_SCALE
    z = read_word_2c(GYRO_ZOUT) / GYRO_SCALE
    return x, y, z

def calculate_angle():
    accel_data = get_acceleration_data()
    x_accel, y_accel, z_accel = accel_data

    roll = math.atan2(y_accel, z_accel) * (180.0 / math.pi)
    #pitch = math.atan(-x_accel / math.sqrt(y_accel * y_accel + z_accel * z_accel)) * (180.0 / math.pi)

    gyro_data = get_rotation_data()
    x_gyro, y_gyro, z_gyro = gyro_data

    roll_rate = x_gyro
    #pitch_rate = y_gyro

    return roll
roll = calculate_angle()

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
    
while True:
    
    
    
# Example usage:
    
    roll = calculate_angle()
    print(f"Roll: {roll:.2f} degrees")
    sleep(0.1)
    
    if roll <=0:
        rotate_clockwise(360)
        time.sleep(0.001)
# Rotate the motor 180 degrees counterclockwise with a 2ms delay between steps
    else:
        rotate_counterclockwise(360)
        time.sleep(0.001)

