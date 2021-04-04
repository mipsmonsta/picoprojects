from machine import Pin, ADC, PWM
import utime, math
from servo import Servo

xAxis = ADC(Pin(26))
yAxis = ADC(Pin(27))

swButton = Pin(16, Pin.IN, Pin.PULL_UP)

#servo pinout and config
servo = Servo(17)    

def readJoystickRaw():
    x = xAxis.read_u16()
    y = yAxis.read_u16()
    btnV = swButton.value()
    return x, y, btnV

def readJoystickTheta(x, y):
    middle = 34000
    y = int(math.ceil(y/1000.0)*1000)
    x = int(math.ceil(x/1000.0)*1000)
    
    angleRad = math.atan2((y - middle),(x - middle))
    
    angle = int(angleRad * 180 /math.pi)
    return angle

try:
    while True:
        #input("read sensor")
        x, y, btnV = readJoystickRaw()
        theta = readJoystickTheta(x, y)
        servo.angle(theta)
        print("x: %s, y: %s, sw: %s, angle: %s" % (str(x), str(y), str(btnV), str(theta)))
        utime.sleep(0.4)
finally:
    servo.deinit()
    print("Goodbye")