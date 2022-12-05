import re

f = open("input5.txt", "r")
first_line = f.readline()
num_stacks = int(len(first_line) / 4)

stacks = {}
for i in range(1, num_stacks + 1):
    stacks[i] = []

splitter = ""
for idx in stacks:
    splitter += f" {idx}  "
splitter = splitter[:-1] + "\n\n"

f.seek(0)
whole_input = f.read().split(splitter)
stacks_input = whole_input[0].splitlines()
moves_input = whole_input[1].splitlines()

regex = ""
for idx in stacks:
    regex += "(\[.\]|.  ) "
regex = regex[:-1]

for input in stacks_input:
    crates = re.match(regex, input)
    for idx in stacks:
        if crates.group(idx) != "   ":
            stacks[idx].append(crates.group(idx)[1:2])

for idx in stacks:
    stacks[idx].reverse()

for input in moves_input:
    parse = re.match("move (.+) from (.) to (.)", input)
    count = int(parse.group(1)) * -1
    source = int(parse.group(2))
    target = int(parse.group(3))
    crates = stacks[source][count:]
    stacks[source] = stacks[source][:count]
    stacks[target] = stacks[target] + crates

result = ""
for idx in stacks:
    result = result + stacks[idx][-1]
print(result)
