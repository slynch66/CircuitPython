import time
import board
import touchio
import pulseio
from adafruit_motor import servo
 
 
angle = 179    # creates the variable for the servo angle
 
touch_pad = board.A0     # "touch_pad" is a variable for the capacitive touch and here it is assigned to pin 0
touch_pad1 = board.A1

touch = touchio.TouchIn(touch_pad)    # TouchIn is reading the state of the capacitive touch, similar to digitalRead() for Arduino
touch1 = touchio.TouchIn(touch_pad1)
 
# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
 
# Finish coding in the servo
my_servo = servo.Servo(pwm)
 

while True:     # This while True statement is saying if I only touch one of the wires, move the servo that way
    if touch.value and not touch1.value and angle < 180:   
        angle += 1
    if touch1.value and not touch.value and angle > 0:
        angle -= 1
    print(angle)
    my_servo.angle = angle
    time.sleep(.01)
