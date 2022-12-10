import advent
import curses

inputs = advent.re_input("(....) ?(-?\d{0,9})?", 10)


def render_cycle(stdscr, cycle, x):
    horiz = cycle % 40
    if horiz - 1 <= x <= horiz + 1:
        pixel = "█"
    else:
        pixel = " "
    stdscr.addstr(cycle // 40, horiz, pixel, curses.color_pair(1))


def main(stdscr):
    cycle = 0
    x = 1
    curses.curs_set(False)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.start_color()
    stdscr.clear()
    for this_input in inputs:
        command = this_input[0]
        value = int(this_input[1]) if this_input[1] else 0
        render_cycle(stdscr, cycle, x)
        cycle += 1
        if command == "addx":
            render_cycle(stdscr, cycle, x)
            cycle += 1
            x += value

    stdscr.refresh()
    stdscr.getkey()


curses.wrapper(main)
