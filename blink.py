import machine
import utime
Led= machine.Pin("LED" machine.Pin.OUT)
for i in range(20):
    Led.value(1)
    utime.sleep(1)
    print(Led.value())
    Led.value(0)
    utime.sleep(1)
    print(Led.value())