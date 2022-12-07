import re
import advent

inputs = advent.get_input(7).splitlines()

answer = 0

path = ["/"]
dirs = {"/": 0}

for input in inputs:
    if input[0] == "$":  # command
        command = re.match("\$ (..) ?(.*)", input).groups()
        if command[0] == "cd":
            if command[1] == "/":
                path = ["/"]
            elif command[1] == "..":
                path.pop()
            else:
                path.append("".join(path) + "/" + command[1])
        else:
            continue  # ls command - nothing to do
    elif input[0:3] == "dir":
        continue  # dir lines aren't useful
    else:  # this is a file
        size = int(re.match("(\d*).*", input).group(1))
        for p in path:  # add the size to all dirs in the path
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
    if answer >= size >= target:
        answer = size

print(answer)
