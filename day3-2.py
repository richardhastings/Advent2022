import re

f = open("input3.txt", "r")
inputs = f.read().splitlines()

total = 0
buffer = []
for input in inputs:
    buffer.append(input)
    if len(buffer) < 3:
        continue
    for char in buffer[0]:
        if char in buffer[1] and char in buffer[2]:
            if ord(char) >= 97:
                total += ord(char) - 96
            else:
                total += ord(char) - 64 + 26
            break
    buffer = []

print(total)
