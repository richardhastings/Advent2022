import advent
import sys

sys.setrecursionlimit(10000)

grid = advent.get_input(12).splitlines()

start_x = None
start_y = None
max_x = len(grid[0]) - 1
max_y = len(grid) - 1
min_steps = []
answer = 10000


for r_idx, row in enumerate(grid):
    min_steps.append([])
    for t_idx, spot in enumerate(row):
        min_steps[r_idx].append(10000)
        if spot == "S":
            start_x = r_idx
            start_y = t_idx


def step(y, x, prev_height, steps, direction):
    global answer
    this_height = ord(grid[y][x]) - 96

    # reset check
    if grid[y][x] == "S":
        this_height = 0
        steps = 0
    if grid[y][x] == "a":
        this_height = 1
        steps = 0

    # end check
    if grid[y][x] == "E":
        if prev_height >= 25:
            if answer > steps:
                answer = steps
            print("found E in ", steps)
        return

    if this_height > prev_height + 1:
        # too high
        return

    if min_steps[y][x] <= steps:
        # too far
        return

    min_steps[y][x] = steps

    # step:
    if direction != "L" and x + 1 <= max_x:
        step(y, x + 1, this_height, steps + 1, "R")
    if direction != "R" and x - 1 >= 0:
        step(y, x - 1, this_height, steps + 1, "L")
    if direction != "U" and y + 1 <= max_y:
        step(y + 1, x, this_height, steps + 1, "D")
    if direction != "D" and y - 1 >= 0:
        step(y - 1, x, this_height, steps + 1, "U")
    return


step(start_x + 1, start_y, 0, 1, "R")
print(answer)
advent.clip(answer)
