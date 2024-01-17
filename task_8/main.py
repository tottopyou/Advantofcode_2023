from data import *
import re

direction = info.split('\n')[0]*100000

variants = info.split('\n')

variants.pop(0)
variants.pop(0)
variant = {}

for var in variants:
    variant[var[:3]] = var[7:10] + var[12:15]

answer = "AAA"

for i, direct in enumerate(direction):
    if direct == 'L':
        answer = variant[answer][:3]
    elif direct == 'R':
        answer = variant[answer][3:]
    if answer == "ZZZ":
        print(i+1)
        break

