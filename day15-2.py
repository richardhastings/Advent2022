import advent

inputs = advent.re_input(
    "Sensor at x=([\d-]*), y=([\d-]*): closest beacon is at x=([\d-]*), y=([\d-]*)", 15
)

max = 4000001

sensors = []

for i in inputs:
    sensor_x = int(i[0])
    sensor_y = int(i[1])
    beacon_x = int(i[2])
    beacon_y = int(i[3])

    distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y) + 1

    sensors.append({"x": sensor_x, "y": sensor_y, "dist": distance})

for target_y in range(max):
    print(target_y)
    target_x = 0
    while target_x < max:
        for s in sensors:
            found = False
            distance = s["dist"] - abs(target_y - s["y"])
            if distance > (abs(target_x - s["x"])):
                found = True
                target_x = s["x"] + distance
                break
        if not found:
            print("answer is", target_y, target_x, target_x * 4000000 + target_y)
            quit()
