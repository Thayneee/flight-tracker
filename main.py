import json

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



