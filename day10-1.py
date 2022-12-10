import advent

inputs = advent.re_input("(....) ?(-?\d{0,9})?", 10)

answer = 0
cycle = 0
x = 1


def check_cycle():
    if cycle % 40 == 20:
        return x * cycle
    return 0


for this_input in inputs:
    command = this_input[0]
    value = int(this_input[1]) if this_input[1] else 0

    cycle += 1
    answer += check_cycle()
    if command == "addx":
        cycle += 1
        answer += check_cycle()
        x += value


print(answer)
advent.clip(answer)
