import advent

grid = advent.get_input(8).splitlines()

answer = 0

for r_idx, row in enumerate(grid):
    for t_idx, tree in enumerate(row):
        count = 0
        for g in grid[r_idx + 1 :]:
            count += 1
            if tree <= g[t_idx]:
                break
        score = count

        count = 0
        for g in reversed(grid[:r_idx]):
            count += 1
            if tree <= g[t_idx]:
                break
        score = score * count

        count = 0
        for g in grid[r_idx][t_idx + 1 :]:
            count += 1
            if tree <= g:
                break
        score = score * count

        count = 0
        for g in reversed(grid[r_idx][:t_idx]):
            count += 1
            if tree <= g:
                break
        score = score * count

        if score > answer:
            answer = score


print(answer)
advent.clip(answer)
