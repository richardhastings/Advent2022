import re

outcomes = {
    'A': {'X':3, 'Y':6, 'Z':0},
    'B': {'X':0, 'Y':3, 'Z':6},
    'C': {'X':6, 'Y':0, 'Z':3}
    }

shape_score = {
    'X':1,
    'Y':2,
    'Z':3
}

f = open("input2.txt", "r")
inputs = f.read().splitlines()

score = 0
for input in inputs:
    shapes = input.split(' ')
    score += outcomes[shapes[0]][shapes[1]]
    score += shape_score[shapes[1]]

print(score)