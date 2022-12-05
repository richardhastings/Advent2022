import re

f = open("input3.txt", "r")
inputs = f.read().splitlines()

total = 0
for input in inputs:
    half = len(input) // 2
    for char in input[0:half]:
        if char in input[half:]:
            if ord(char) >= 97:
                total += ord(char) - 96
            else:
                total += ord(char) - 64 + 26
            break

print(total)
