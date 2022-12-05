import re

score_1 = {
    'A': {'X':3, 'Y':1, 'Z':2},
    'B': {'X':1, 'Y':2, 'Z':3},
    'C': {'X':2, 'Y':3, 'Z':1}
    }

score_2 = {
    'X':0,
    'Y':3,
    'Z':6
}

f = open("input2.txt", "r")
inputs = f.read().splitlines()

score = 0
for input in inputs:
    shapes = input.split(' ')
    score += score_1[shapes[0]][shapes[1]]
    score += score_2[shapes[1]]

print(score)