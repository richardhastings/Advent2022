f = open("input1.txt", "r")
inputs = f.read().split("\n\n")

elves = []

for input in inputs:
    calories = [int(cal) for cal in input.splitlines()]
    elves.append(sum(calories))

ordered = sorted(elves, reverse=True)
print("total", sum(ordered[0:3]))
