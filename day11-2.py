import advent

monkey_inputs = advent.get_input(11).split("\n\n")

monkeys = []
worry_factor = 1

for monkey_input in monkey_inputs:
    monkey_elements = monkey_input.splitlines()
    monkey_id = int(monkey_elements[0][7:8])
    monkeys.append({"inspects": 0})
    monkeys[monkey_id]["items"] = [
        int(item) for item in monkey_elements[1][18:].split(", ")
    ]
    monkeys[monkey_id]["operation"] = monkey_elements[2][23:24]
    monkeys[monkey_id]["operand"] = monkey_elements[2][25:]
    monkeys[monkey_id]["test"] = int(monkey_elements[3][21:])
    monkeys[monkey_id]["if_true"] = int(monkey_elements[4][29:])
    monkeys[monkey_id]["if_false"] = int(monkey_elements[5][30:])
    worry_factor = worry_factor * monkeys[monkey_id]["test"]

for round in range(10000):
    for monkey in monkeys:
        for item in monkey["items"]:
            operand = monkey["operand"]
            if operand == "old":
                operand = item
            else:
                operand = int(operand)
            if monkey["operation"] == "+":
                item = item + operand
            else:
                item = item * operand
            monkey["inspects"] += 1
            if item % monkey["test"] == 0:
                monkeys[monkey["if_true"]]["items"].append(item % worry_factor)
            else:
                monkeys[monkey["if_false"]]["items"].append(item % worry_factor)
        monkey["items"] = []


answer = [monkey["inspects"] for monkey in monkeys]
answer = sorted(answer, reverse=True)
answer = answer[0] * answer[1]
print(answer)
advent.clip(answer)
