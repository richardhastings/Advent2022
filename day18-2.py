import advent

UNKNOWN = 0
LAVA = 1
EXTERNAL = 2
INTERNAL = 3

MIN = 0
MAX = 21

coords = advent.re_input("(\d*),(\d*),(\d*)", 18)
grid = []

for x in range(MAX + 1):
    grid.append([])
    for y in range(MAX + 1):
        grid[x].append([])
        for z in range(MAX + 1):
            grid[x][y].append(UNKNOWN)

for y in range(MAX + 1):
    for z in range(MAX + 1):
        grid[MIN][y][z] = EXTERNAL
        grid[MAX][y][z] = EXTERNAL

for x in range(MAX + 1):
    for z in range(MAX + 1):
        grid[x][MIN][z] = EXTERNAL
        grid[x][MAX][z] = EXTERNAL

for x in range(MAX + 1):
    for y in range(MAX + 1):
        grid[x][y][MIN] = EXTERNAL
        grid[x][y][MAX] = EXTERNAL

for cube in coords:
    grid[int(cube[0])][int(cube[1])][int(cube[2])] = LAVA

for i in range(MAX):
    for x in range(MAX):
        for y in range(MAX):
            for z in range(MAX):
                if grid[x][y][z] == UNKNOWN:
                    if (
                        grid[x + 1][y][z] == EXTERNAL
                        or grid[x - 1][y][z] == EXTERNAL
                        or grid[x][y + 1][z] == EXTERNAL
                        or grid[x][y - 1][z] == EXTERNAL
                        or grid[x][y][z + 1] == EXTERNAL
                        or grid[x][y][z - 1] == EXTERNAL
                    ):
                        grid[x][y][z] = EXTERNAL

for x in range(MAX):
    for y in range(MAX):
        for z in range(MAX):
            if grid[x][y][z] == UNKNOWN:
                grid[x][y][z] = INTERNAL

answer = 0

for x in range(MAX):
    for y in range(MAX):
        for z in range(MAX):
            if grid[x][y][z] == LAVA:
                if grid[x + 1][y][z] == EXTERNAL:
                    answer += 1
                if grid[x - 1][y][z] == EXTERNAL:
                    answer += 1
                if grid[x][y + 1][z] == EXTERNAL:
                    answer += 1
                if grid[x][y - 1][z] == EXTERNAL:
                    answer += 1
                if grid[x][y][z + 1] == EXTERNAL:
                    answer += 1
                if grid[x][y][z - 1] == EXTERNAL:
                    answer += 1

print(answer)
advent.clip(answer)
