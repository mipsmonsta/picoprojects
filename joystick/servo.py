from machine import Pin, PWM #for pico
import utime # pico

class Servo:
    DELAY_FOR_MOVT = 0.015
    DEGREE_TOLERANCE = 3
    def __init__(self, pin, minVal=2300, maxVal=7700):
        self._pwm = None
        if isinstance(pin, int):
            self._pwm = PWM(Pin(pin))
        elif isinstance(pin, PWM):
            self._pwm = pin
        self._pwm.freq(50) #50 hz 
        self.lowerLimit = minVal
        self.upperLimit = maxVal
        self._goto(self.lowerLimit) # goto middle
        self.prevAngle = 0
        
    def _goto(self, value):
        """
        Goto to value between lowerLimit and upperLimit 
        """
        if value < self.lowerLimit:
            value = self.lowerLimit
        elif value > self.upperLimit:
            value = self.upperLimit
        self._pwm.duty_u16(value)
        utime.sleep(Servo.DELAY_FOR_MOVT)
        
    def angle(self, theta):
        if theta < 0 or theta > 180:
            return            
        if abs(theta - self.prevAngle) < Servo.DEGREE_TOLERANCE:
            return
        print("accepted theta %s" % str(theta))
        self.prevAngle = theta #remember for next call of angle to check tolerance
        pwm_duty = self.lowerLimit + int((self.upperLimit - self.lowerLimit) * (theta / 180))
        self._goto(pwm_duty)
        
    def deinit(self):
        self._pwm.deinit()
        
        