from data import *
import re

direction = info.split('\n')[0]*1000000

variants = info.split('\n')

variants.pop(0)
variants.pop(0)
variant = {}
answer = []
j = 0
bool = False

for var in variants:
    variant[var[:3]] = var[7:10] + var[12:15]


for item in variant.keys():
    if item[2] == "A":
        answer.append(item)
        print(item)

for i, direct in enumerate(direction):
    for _ in range(len(answer)):
        if direct == 'L':
            answer.append(variant[answer[0]][:3])
            answer.pop(0)
        elif direct == 'R':
            answer.append(variant[answer[0]][3:])
            answer.pop(0)
    for res in answer:
        if res[2] == "Z":
            j+= 1
        if j == len(answer):
            print(i+1)
            bool = True
            break
    if bool == True:
        print(answer)
        break
    else:
        print(j)
        j = 0
