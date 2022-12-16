import advent
import re
import json

inputs = advent.re_input(
    "Sensor at x=([\d-]*), y=([\d-]*): closest beacon is at x=([\d-]*), y=([\d-]*)", 15
)

answer = 0

target_row = {}
target_y = 2000000

for i in inputs:
    sensor_x = int(i[0])
    sensor_y = int(i[1])
    beacon_x = int(i[2])
    beacon_y = int(i[3])

    if sensor_y == target_y:
        target_row[sensor_x] = "S"
    if beacon_y == target_y:
        target_row[beacon_x] = "B"

    distance = (
        abs(beacon_x - sensor_x)
        + abs(beacon_y - sensor_y)
        - abs(target_y - sensor_y)
        + 1
    )
    if distance > 0:
        for x in range(distance):
            for point in [sensor_x + x, sensor_x - x]:
                if not target_row.get(point):
                    target_row[point] = "#"
                    answer += 1

print(answer)
advent.clip(answer)
