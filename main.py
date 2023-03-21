import json
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

lcd = I2cLcd(1, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

with open("aircraft.json", "r") as f:
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

#for i in range(len(squawk)):
#    print(squawk[i], flight[i], altitude[i], speed[i])

lcd.move_to(0,1)
lcd.putstr(f"Flight {flight[0]} is")
lcd.move_to(0,2)
lcd.putstr(f"{altitude[0]} feet above right now!")
lcd.move_to(0,3)
lcd.putstr(f"Going {speed[0]} knots.")

