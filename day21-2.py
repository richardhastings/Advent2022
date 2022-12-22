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
        parse = re.match("(....) (.) (....)", op)
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
            case '=':
                return (value1, value2)


low = 1
test = 10000000000000
high = 20000000000000

monkeys["root"] = monkeys["root"].replace("+", "=")
monkeys["humn"] = test
answer = get_monkey_value("root")

while not answer[0] == answer[1]:
    if answer[0] > answer[1]:
        low = test
        test = test + ((high - test) / 2)
    else:
        high = test
        test = low + ((test - low) / 2)
    monkeys["humn"] = test
    answer = get_monkey_value("root")
    print(low, test, high)
    print(answer)

print(int(test))
advent.clip(int(test))
