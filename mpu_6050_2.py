import machine
from machine import Pin, I2C
import math

# ... (previous code)

def calculate_angles(accel_data):
    accel_x, accel_y, accel_z = accel_data

    roll = math.atan2(accel_y, math.sqrt(accel_x ** 2 + accel_z ** 2))
    pitch = math.atan2(-accel_x, math.sqrt(accel_y ** 2 + accel_z ** 2))

    roll_deg = math.degrees(roll)
    pitch_deg = math.degrees(pitch)

    return roll_deg, pitch_deg

if __name__ == "__main__":
    i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
    mpu6050_init(i2c)
    
    while True:
        accel_data = mpu6050_get_accel(i2c)
        gyro_data = mpu6050_get_gyro(i2c)

        roll, pitch = calculate_angles(accel_data)

        print("Accelerometer:\t", accel_data, "g")
        print("Gyroscope:\t", gyro_data, "°/s")
        print("Roll:\t\t", roll, "degrees")
        print("Pitch:\t\t", pitch, "degrees")
