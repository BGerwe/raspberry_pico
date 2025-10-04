from machine import Pin, I2C
import utime
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from mfrc522 import MFRC522

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

# RFID setup
#rdr = MFRC522(spi_id=0, sck=2, mosi=3, miso=4, rst=6, cs=5)
rdr = MFRC522(spi_id=1, sck=10, mosi=11, miso=12, rst=14, cs=13)


def read_rfid():
    (status, tag_type) = rdr.request(rdr.REQIDL)
    if status == rdr.OK:
        (stat, uid) = rdr.SelectTagSN()
        if stat == rdr.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            return str(card)
    return None


while True:
    lcd.clear()
    lcd.putstr("Scan RFID tag...")
    utime.sleep(.5)
   
    card = read_rfid()
    if card:
        lcd.clear()
        lcd.putstr(card)
        utime.sleep(2)
       
    else:
            lcd.clear()
            lcd.putstr("No tag detected")
            utime.sleep(.5)
           
utime.sleep_ms(500)
