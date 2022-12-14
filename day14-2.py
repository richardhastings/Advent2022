import advent

inputs = advent.get_input(14).splitlines()

answer = 0

grid = [["." for x in range(400)] for y in range(200)]

x_adjust = 300
sand_x = 500 - x_adjust
sand_y = 0
max_y = 0

grid[sand_y][sand_x] = "+"

paths = [i.split(" -> ") for i in inputs]
paths = [[coord.split(",") for coord in p] for p in paths]
for path in paths:
    for idx in range(len(path) - 1):
        from_x = int(path[idx][0]) - x_adjust
        from_y = int(path[idx][1])
        to_x = int(path[idx + 1][0]) - x_adjust
        to_y = int(path[idx + 1][1])
        if to_y + 2 > max_y:
            max_y = to_y + 2
        if from_y + 2 > max_y:
            max_y = from_y + 2
        if from_x == to_x:
            if from_y < to_y:
                rng = range(from_y, to_y + 1)
            else:
                rng = range(to_y, from_y + 1)
            for y in rng:
                grid[y][from_x] = "#"
        else:
            if from_x < to_x:
                rng = range(from_x, to_x + 1)
            else:
                rng = range(to_x, from_x + 1)
            for x in rng:
                grid[from_y][x] = "#"


for x in range(400):
    grid[max_y][x] = "#"


this_sand_x = sand_x
this_sand_y = sand_y
while grid[sand_y][sand_x] == "+":
    this_sand_x = sand_x
    this_sand_y = sand_y
    while True:
        if grid[this_sand_y + 1][this_sand_x] == ".":
            this_sand_y = this_sand_y + 1
        elif grid[this_sand_y + 1][this_sand_x - 1] == ".":
            this_sand_y = this_sand_y + 1
            this_sand_x = this_sand_x - 1
        elif grid[this_sand_y + 1][this_sand_x + 1] == ".":
            this_sand_y = this_sand_y + 1
            this_sand_x = this_sand_x + 1
        else:
            grid[this_sand_y][this_sand_x] = "o"
            answer += 1
            break

print(answer)
advent.clip(answer)
