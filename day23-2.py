import advent

inputs = advent.get_input(23).splitlines()

elves = []

for y in range(len(inputs)):
    for x in range(len(inputs[y])):
        if inputs[y][x] == "#":
            elves.append({"pos": (y + 100000, x + 100000), "proposed": None})

elf_cache = ""


def build_elf_cache():
    global elf_cache
    elf_cache = ""
    for elf in elves:
        y = elf["pos"][0]
        x = elf["pos"][1]
        elf_cache = elf_cache + "|y" + str(y) + "x" + str(x)


def is_elf_at(y, x):
    cache_check = "|y" + str(y) + "x" + str(x)
    return elf_cache.find(cache_check) >= 0


def move_N(elf, y, x):
    elf["proposed"] = (y - 1, x)
    proposed.append((y - 1, x))


def move_S(elf, y, x):
    elf["proposed"] = (y + 1, x)
    proposed.append((y + 1, x))


def move_W(elf, y, x):
    elf["proposed"] = (y, x - 1)
    proposed.append((y, x - 1))


def move_E(elf, y, x):
    elf["proposed"] = (y, x + 1)
    proposed.append((y, x + 1))


proposed = [True]
round = -1
while len(proposed) > 0:
    round += 1
    print(round)
    proposed = []
    build_elf_cache()
    for elf in elves:
        y = elf["pos"][0]
        x = elf["pos"][1]
        NW = is_elf_at(y - 1, x - 1)
        N = is_elf_at(y - 1, x)
        NE = is_elf_at(y - 1, x + 1)
        W = is_elf_at(y, x - 1)
        E = is_elf_at(y, x + 1)
        SW = is_elf_at(y + 1, x - 1)
        S = is_elf_at(y + 1, x)
        SE = is_elf_at(y + 1, x + 1)
        if NW or N or NE or W or E or SW or S or SE:
            match round % 4:
                case 0:
                    if not (NE or N or NW):
                        move_N(elf, y, x)
                    elif not (SE or S or SW):
                        move_S(elf, y, x)
                    elif not (NW or W or SW):
                        move_W(elf, y, x)
                    elif not (NE or E or SE):
                        move_E(elf, y, x)
                case 1:
                    if not (SE or S or SW):
                        move_S(elf, y, x)
                    elif not (NW or W or SW):
                        move_W(elf, y, x)
                    elif not (NE or E or SE):
                        move_E(elf, y, x)
                    elif not (NE or N or NW):
                        move_N(elf, y, x)
                case 2:
                    if not (NW or W or SW):
                        move_W(elf, y, x)
                    elif not (NE or E or SE):
                        move_E(elf, y, x)
                    elif not (NE or N or NW):
                        move_N(elf, y, x)
                    elif not (SE or S or SW):
                        move_S(elf, y, x)
                case 3:
                    if not (NE or E or SE):
                        move_E(elf, y, x)
                    elif not (NE or N or NW):
                        move_N(elf, y, x)
                    elif not (SE or S or SW):
                        move_S(elf, y, x)
                    elif not (NW or W or SW):
                        move_W(elf, y, x)

    for elf in elves:
        if elf["proposed"]:
            if proposed.count(elf["proposed"]) == 1:
                elf["pos"] = elf["proposed"]
            elf["proposed"] = None


answer = round + 1

print(answer)
advent.clip(answer)
