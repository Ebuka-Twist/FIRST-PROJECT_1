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
def control_motor(current_speed, direction):
    if direction == 1:
        IN1_PIN.value(1)
        IN2_PIN.value(0)
        
    if direction == -1:
        IN1_PIN.value(0)
        IN2_PIN.value(1)
    pwm.duty_u16(int(current_speed * 1023 / 100))
    
def compute(current_speed):
    kp = 10
    ki = 0.1
    kd = 2
    error =0
    setpoint = 500
    current_speed = 200
    integral =0
    prev_error = 0
    error = setpoint - current_speed
    integral += error
    derivative = error - prev_error
    prev_error = error
    
    return kp * error + ki * integral + kd * derivative
        
        
try:
    while True:
        #output = kp * error + ki * integral + kd * derivative
       
                
        
        output = compute(200)
        control_motor(output, 1)  # Run the motor at 50% speed in forward direction
        utime.sleep(5)
        print("D")
        
        control_motor(0, 0)
        utime.sleep(5)
        print("E")
        
        control_motor(output, -1)
        utime.sleep(5)
except KeyboardInterrupt:
    pass

# Turn off the motor
pwm.deinit()
 
          