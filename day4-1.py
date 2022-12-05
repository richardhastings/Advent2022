import re

f = open("input4.txt", "r")
inputs = f.read().splitlines()

total=0
for input in inputs:
    parse = re.match('(.+)-(.+),(.+)-(.+)',input)
    start1 = int(parse.group(1))
    end1 = int(parse.group(2))
    start2 = int(parse.group(3))
    end2 = int(parse.group(4))
    if (
        (start1 >= start2 and end1 <= end2)
        or (start2 >= start1 and end2<= end1)
    ):
        print(input)
        total += 1

print(total)
