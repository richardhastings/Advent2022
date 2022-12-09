import advent
import time
import curses


def main(stdscr):
    curses.curs_set(False)
    inputs = advent.re_input("(.) (\d{1,9})", 9)

    answer = 0

    rope_x = [35 for r in range(10)]
    rope_y = [35 for r in range(10)]

    visited = [[0 for s in range(70)] for r in range(70)]

    for this_input in inputs:
        stdscr.clear()
        direction = this_input[0]
        distance = int(this_input[1])
        for step in range(distance):
            # move head:
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
                    if (
                        rope_x[knot - 1] > rope_x[knot]
                        and rope_y[knot - 1] > rope_y[knot]
                    ):
                        rope_y[knot] += 1
                        rope_x[knot] += 1
                    elif (
                        rope_x[knot - 1] > rope_x[knot]
                        and rope_y[knot - 1] < rope_y[knot]
                    ):
                        rope_y[knot] -= 1
                        rope_x[knot] += 1
                    elif (
                        rope_x[knot - 1] < rope_x[knot]
                        and rope_y[knot - 1] > rope_y[knot]
                    ):
                        rope_y[knot] += 1
                        rope_x[knot] -= 1
                    elif (
                        rope_x[knot - 1] < rope_x[knot]
                        and rope_y[knot - 1] < rope_y[knot]
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

        for knot in reversed(range(10)):
            stdscr.addstr(rope_y[knot], rope_x[knot], str(knot))
        stdscr.refresh()
        time.sleep(0.03)

    for row in visited:
        answer += sum(row)

    print(answer)
    advent.clip(answer)


curses.wrapper(main)
