import advent

inputs = advent.get_input(25).splitlines()


answer = ""
total = 0

for number in inputs:
    value = 0
    for idx, digit in enumerate(number[::-1]):
        if digit == "=":
            digit_value = -2
        elif digit == "-":
            digit_value = -1
        else:
            digit_value = int(digit)

        value += digit_value * (5 ** idx)
    total += value

for idx in reversed(range(50)):
    max_neg = 0
    for idx2 in range(idx):
        max_neg = max_neg + -2 * (5 ** idx2)
    pos_2 = 2 * (5 ** idx)
    pos_1 = 5 ** idx
    neg_1 = -1 * (5 ** idx)
    neg_2 = -2 * (5 ** idx)

    if total >= pos_2 + max_neg:
        answer += "2"
        total = total - pos_2
    elif total >= pos_1 + max_neg:
        answer += "1"
        total = total - pos_1
    elif total >= max_neg:
        answer += "0"
    elif total >= neg_1 + max_neg:
        answer += "-"
        total = total - neg_1
    else:
        answer += "="
        total = total - neg_2

answer = answer.lstrip("0")
print(answer)
advent.clip(answer)
