import advent
import re

inputs = advent.re_input("(....): (.*)", 21)

monkeys = {}

for i in inputs:
    monkeys[i[0]] = i[1]

print(monkeys)

def get_monkey_value(name):
    op = monkeys[name]
    try:
        return int(op)
    except ValueError as e:
        parse = re.match('(....) (.) (....)',op)
        value1 = get_monkey_value(parse.group(1))
        value2 = get_monkey_value(parse.group(3))
        operation = parse.group(2)
        match operation:
            case '+':
                return value1 + value2
            case '*':
                return value1 * value2
            case '-':
                return value1 - value2
            case '/':
                return value1 / value2

answer = get_monkey_value('root')

print(answer)
advent.clip(answer)
