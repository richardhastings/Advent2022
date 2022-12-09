import advent

inputs = advent.re_input("(.) (\d{1,9})", 9)

answer = 0

rope_x = [2000 for r in range(10)]
rope_y = [2000 for r in range(10)]

visited = [[0 for s in range(4000)] for r in range(4000)]

for this_input in inputs:
    direction = this_input[0]
    distance = int(this_input[1])
    for step in range(distance):
        #move head:
        match direction:
            case 'U':
                rope_y[0] += 1
            case 'D':
                rope_y[0] -= 1
            case 'L':
                rope_x[0] -= 1
            case 'R':
                rope_x[0] += 1

        # move tails
        for knot in range(1, 10):
            if (
                abs(rope_x[knot - 1] - rope_x[knot]) > 1
                and abs(rope_y[knot - 1] - rope_y[knot]) >= 1
            ) or (
                abs(rope_x[knot - 1] - rope_x[knot]) >= 1
                and abs(rope_y[knot - 1] - rope_y[knot]) > 1
            ):
                # diagonal:
                if rope_x[knot - 1] > rope_x[knot] and rope_y[knot - 1] > rope_y[knot]:
                    rope_y[knot] += 1
                    rope_x[knot] += 1
                elif (
                    rope_x[knot - 1] > rope_x[knot] and rope_y[knot - 1] < rope_y[knot]
                ):
                    rope_y[knot] -= 1
                    rope_x[knot] += 1
                elif (
                    rope_x[knot - 1] < rope_x[knot] and rope_y[knot - 1] > rope_y[knot]
                ):
                    rope_y[knot] += 1
                    rope_x[knot] -= 1
                elif (
                    rope_x[knot - 1] < rope_x[knot] and rope_y[knot - 1] < rope_y[knot]
                ):
                    rope_y[knot] -= 1
                    rope_x[knot] -= 1

            elif rope_x[knot - 1] > rope_x[knot] + 1:
                rope_x[knot] += 1
            elif rope_x[knot - 1] < rope_x[knot] - 1:
                rope_x[knot] -= 1
            elif rope_y[knot - 1] > rope_y[knot] + 1:
                rope_y[knot] += 1
            elif rope_y[knot - 1] < rope_y[knot] - 1:
                rope_y[knot] -= 1

        visited[rope_x[9]][rope_y[9]] = 1

for row in visited:
    answer += sum(row)

print(answer)
advent.clip(answer)
