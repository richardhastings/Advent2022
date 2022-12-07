import re
import advent

inputs = advent.get_input(7).splitlines()

answer = 0

path = ["/"]
dirs = {"/": 0}

for input in inputs:
    if input[0] == "$":  # command
        parse = re.match("\$ (..) ?(.*)", input)
        if parse.group(1) == "cd":
            if parse.group(2) == "/":
                path = ["/"]
            elif parse.group(2) == "..":
                path.pop()
            else:
                path.append("".join(path) + "/" + parse.group(2))
        else:
            continue
    elif input[0:3] == "dir":
        continue
    else:
        parse = re.match("(\d*) (.*)", input)
        size = int(parse.group(1))
        for p in path:
            if p in dirs:
                dirs[p] += size
            else:
                dirs[p] = size

for name, size in dirs.items():
    if size <= 100000:
        answer += size

print(answer)

# part 2

target = 30000000 - (70000000 - dirs["/"])
answer = 70000000

for name, size in dirs.items():
    if size >= target:
        if size <= answer:
            answer = size

print(answer)
