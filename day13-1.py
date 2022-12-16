import advent
import re
import json

input_pairs = advent.get_input(13).split("\n\n")

answer = 0


def parse_array_pair(array1, array2):
    print(array1, " ! ", array2)

    if len(array1) == 0 and len(array2) > 0:
        print("Left side ran out of items, so inputs are in the right order")
        return 1
    if len(array1) == 0 and len(array2) == 0:
        print("Both empty arrays - inconclusive")
        return 0
    for idx in range(len(array1)):
        if len(array2) <= idx:
            print("Right side ran out of items, so inputs are not in the right order")
            return -1
        print("loop ", array1[idx], " ! ", array2[idx])
        if (isinstance(array1[idx], int)) and (isinstance(array2[idx], int)):
            print("both is int")
            if int(array1[idx]) < int(array2[idx]):
                print("left is smaller - valid")
                return 1
            elif int(array1[idx]) > int(array2[idx]):
                print("right is smaller - invalid")
                return -1
            else:
                # inconclusive
                continue

        elif not (isinstance(array1[idx], int)) and not (isinstance(array2[idx], int)):
            print("both sides are lists")
            result = parse_array_pair(array1[idx], array2[idx])
            if result != 0:
                return result
            else:
                continue
        elif (isinstance(array1[idx], int)) and not (isinstance(array2[idx], int)):
            print("left is int")
            result = parse_array_pair([array1[idx]], array2[idx])
            if result != 0:
                return result
            else:
                continue
        elif not (isinstance(array1[idx], int)) and (isinstance(array2[idx], int)):
            print("right is int")
            result = parse_array_pair(array1[idx], [array2[idx]])
            if result != 0:
                return result
            else:
                continue

    print("ran out?- valid?")
    return 1


for idx, pair in enumerate(input_pairs):
    pair = pair.splitlines()
    parse1 = json.loads(pair[0])
    parse2 = json.loads(pair[1])
    print("pair ", idx + 1)
    result = parse_array_pair(parse1, parse2)
    if result == 1:
        answer += idx + 1
    print("---------------------------------------------------")


print("===================")
print(answer)
advent.clip(answer)
