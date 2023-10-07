import machine
import utime

# Pin configuration for the motor driver (change these as needed)
PWM_PIN = machine.Pin(20)
IN1_PIN = machine.Pin(19, machine.Pin.OUT)
IN2_PIN = machine.Pin(18, machine.Pin.OUT)

# Set PWM frequency
pwm = machine.PWM(PWM_PIN)
pwm.freq(1000)  # You can adjust the frequency as needed

# Function to control the motor
def control_motor(speed_percent, direction):
    if direction == 1:
        IN1_PIN.value(1)
        IN2_PIN.value(0)
        
    if direction == -1:
        IN1_PIN.value(0)
        IN2_PIN.value(1)
    pwm.duty_u16(int(speed_percent * 65535 / 100))

# Control the motor7
try:
    while True:
        control_motor(100, 1)  # Run the motor at 50% speed in forward direction
        utime.sleep(5)
        
        
        control_motor(0, 0)   # Stop the motor
        utime.sleep(5)
        
        control_motor(80, -1)
        utime.sleep(5)
        
        control_motor(0, 0)
        utime.sleep(2)
except KeyboardInterrupt:
    pass

# Turn off the motor
pwm.deinit()
 
  