f = open("input1.txt", "r")
inputs = f.read().split("\n\n")

max = 0
for input in inputs:
    calories = input.splitlines()
    total = 0
    for cal in calories:
        total += int(cal)
    print(total)
    if total > max:
        max = total
    print("--")

print("max", max)
