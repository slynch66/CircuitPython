import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")           # Makes the serial monitor say "Make it red!" when the LED is red.
while True:                  # While True is basically the Loop command in Arduino.
dot.fill((255,0,0))     #This command makes the neopixel LED on the Metroid light up red.
