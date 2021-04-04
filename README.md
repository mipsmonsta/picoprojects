# Pico Projects
Code Adventures with the Raspberry Pi Pico and Components

### Adventures

1. Joystick and SG90 Servo
- Files: Servo.py and Joystick_Servo.py
  - Servo.py contains the Servo class that has the function Servo::angle that will control the servo to point from 0 to 180 degrees. Internally it sets the PWM duty cycle of the pico pin so as to vary the angle. The Servo class can be initialized with GPIO pin number to become a PWM pin.
  - Joystick_Servo.py is the program file that read the joystick analog values for x-axis and y-axis and use trigonometry to derive angles that are fed to the Servo instance so as to control the SG90 Tower Servo.
