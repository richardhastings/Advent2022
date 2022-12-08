import advent

grid = advent.get_input(8).splitlines()

answer = 0

for r_idx, row in enumerate(grid):
    for t_idx, tree in enumerate(row):
        if (
            all([(tree > g[t_idx]) for g in grid[r_idx + 1 :]])
            or all([(tree > g[t_idx]) for g in grid[:r_idx]])
            or all([(tree > g) for g in grid[r_idx][t_idx + 1 :]])
            or all([(tree > g) for g in grid[r_idx][:t_idx]])
        ):
            answer += 1


print(answer)
advent.clip(answer)
