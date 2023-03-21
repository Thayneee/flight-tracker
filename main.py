import json
import time
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

lcd = I2cLcd(1, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

while True:
    with open("/run/dump1090-mutability/aircraft.json", "r") as f:
        data = json.load(f)

    required_fields = ['squawk', 'flight', 'altitude', 'speed']

    squawk = []
    flight = []
    altitude = []
    speed = []

    for aircraft in data["aircraft"]:
        if all(field in aircraft for field in required_fields):
            squawk.append(aircraft["squawk"])
            flight.append(aircraft["flight"])
            altitude.append(aircraft["altitude"])
            speed.append(aircraft["speed"])

        else:
            continue

    if len(squawk) == 0:
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("There are no planes above.")
        lcd.move_to(0,1)
        lcd.putstr(":(")
    else:
        for i in range(len(squawk)):
            lcd.move_to(0,0)
            lcd.putstr(f"Flight {flight[i]} is")
            lcd.move_to(0,1)
            lcd.putstr(f"{altitude[i]} feet above")
            lcd.move_to(0,2)
            lcd.putstr(f"right now! Going {speed[i]}")
            lcd.move_to(0,3)
            lcd.putstr(f"knots. Squawk: {squawk[i]}")
            time.sleep(3)

