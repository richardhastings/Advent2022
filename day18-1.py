import advent

MIN = 0
MAX = 21

coords = advent.re_input("(\d*),(\d*),(\d*)", 18)
grid = []

for x in range(MAX + 1):
    grid.append([])
    for y in range(MAX + 1):
        grid[x].append([])
        for z in range(MAX + 1):
            grid[x][y].append(False)

for cube in coords:
    grid[int(cube[0])][int(cube[1])][int(cube[2])] = True

answer = 0

for x in range(22):
    for y in range(22):
        for z in range(22):
            if grid[x][y][z]:
                if not grid[x + 1][y][z]:
                    answer += 1
                if not grid[x - 1][y][z]:
                    answer += 1
                if not grid[x][y + 1][z]:
                    answer += 1
                if not grid[x][y - 1][z]:
                    answer += 1
                if not grid[x][y][z + 1]:
                    answer += 1
                if not grid[x][y][z - 1]:
                    answer += 1

print(answer)
advent.clip(answer)
