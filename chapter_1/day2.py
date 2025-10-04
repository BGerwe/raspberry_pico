from machine import I2C, Pin
import utime
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# Some kind of hex address?
I2C_ADDR = 0x27
# Seems like these need to match physical characteristics of LCD board?
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 24

# Initializing something about LCD display driver?
# machine.I2C is a two-wire serial protocol:  https://docs.micropython.org/en/v1.23.0/library/machine.I2C.html#class-i2c-a-two-wire-serial-protocol
# SCL is a clock line and SDA is a dataline.

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

messages = ["Nebula Raider", "Comm System OK", "Incoming Msg", "Awaiting Command", "I love you"]

messages = ["Hi Lindsay", "This is your husband", "I love you"]
while True:
    for message in messages:
        lcd.clear()
        lcd.putstr(message)
        utime.sleep(3)
