import time
import board
import touchio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27.

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

touch_pad = board.A0     # "touch_pad" is a variable for the capacitive touch and here it is assigned to pin 0
touch_pad1 = board.A4

button = touchio.TouchIn(touch_pad)    # TouchIn is reading the state of the capacitive touch, similar to digitalRead() for Arduino
filippe = touchio.TouchIn(touch_pad1)

value = 0         # 'mathe' is the counting variable displayed on the lcd screen
state = 1         # 'state' is whether the counter goes up or down

StateFlipper = False
counterTouched = False




while True:

               # These two if statements make touching the 'switch' wire change the increment from going up to going down and vice versa
    
    if filippe.value and not StateFlipper:
        state = state*-1
        StateFlipper = True
    if not filippe.value:
        StateFlipper = False

               # These two if statements make touching the 'counter' wire change the lcd screen value, based on if the state is positive or negative

    if button.value and not counterTouched:
        value = value + state
        counterTouched = True
    if not button.value:
        counterTouched = False

               # This block of code prints out the value and the increment on the lcd screen on different lines

    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print('Value: ' + str(value))
    lcd.set_cursor_pos(1,0)
    lcd.print('Change: ' + str(state))
    time.sleep(.05)
