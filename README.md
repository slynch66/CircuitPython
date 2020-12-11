# CircuitPython

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
---

## Hello_CircuitPython

### Description:
Hello CircuitPython was an assignment where you setup your Metroid Express along with a code-editing software and your Mac/Chromebook/PC at home. First, [watch the video](https://cvilleschools.instructure.com/courses/31071/assignments/258611?module_item_id=797166) on the assignment. I am using my school Chromebook at home, so I had to install CARET and BEAGLE TERM as my software for editing code/serial monitor. Below is the commented code I used for this assignment.

### [Code](https://github.com/slynch66/CircuitPython/blob/main/Hello_CircuitPython.py):
``` python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")           # Makes the serial monitor say "Make it red!" when the LED is red.
while True:                  # While True is basically the Loop command in Arduino.
dot.fill((255,0,0))     #This command makes the neopixel LED on the Metroid light up red.
```

### Reflection:
For this assignment I learned how to make the neopixel LED light up as a color. The code for this is part of my commented code. The neopixel works with RGB values, so if you want to make it light up a specific color, find the RGB values of that color using Google and then input them into the command:
``` python
dot.fill((0,0,0))
```
For example, if I want my neopixel to light up as cyan, I can search Google to find the RGB values of that color (0,255,255). Then just input those values into your command:
``` python
 dot.fill((0,255,255))
```

## CircuitPython_Servo

[source of code](https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo)

Also shoutout to [Alden's repository](https://github.com/adent11/CircuitPython) for the "While True" statement in my code. 

### Description
For this assignment we were required to make a servo sweep back and forth from 0 to 180 degrees using capacitive touch. When you touch one wire, the servo rotates one way, when you touch the other wire, the servo rotates the other way.

### [Code](https://github.com/slynch66/CircuitPython/blob/main/CircuitPython_Servo.py):
```python
touch_pad = board.A0     # "touch_pad" is a variable for the capacitive touch and here it is assigned to pin 0
touch_pad1 = board.A1

touch = touchio.TouchIn(touch_pad)    # TouchIn is reading the state of the capacitive touch, similar to digitalRead() for Arduino
touch1 = touchio.TouchIn(touch_pad1)

while True:     # This while True statement is saying if I only touch one of the wires, move the servo that way
    if touch.value and not touch1.value and angle < 180:   
        angle += 1
    if touch1.value and not touch.value and angle > 0:
        angle -= 1
    print(angle)
    my_servo.angle = angle
    time.sleep(.01)
```

### Reflection
On this assignment I had a lot of trouble with getting the capacitive touch to work. Here is the [website](https://learn.adafruit.com/circuitpython-essentials/circuitpython-cap-touch) for learning how to use capacitive touch with circuitpython. All you have to do after that is figure out what "while True" statements you need to use.

## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Images

### Reflection

## CircuitPython_Distance_Sensor
A lot of my code came from 

[learn.adafruit.com](https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython)

[learn.Alden.repository](https://github.com/adent11/CircuitPython)
### Description & Code

```python
Code goes here

```

### Evidence

### Images

### Reflection
