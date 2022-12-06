f = open("input6.txt", "r")
inputs = f.read()

marker_length = 14  # part 1 = 4


def has_duplicate_char(input):
    for idx, char in enumerate(input):
        if char in input[idx + 1 :]:
            return True
    return False


for idx in range(marker_length, len(inputs)):
    if has_duplicate_char(inputs[idx - marker_length : idx]):
        continue
    print(idx)
    break
