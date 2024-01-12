from data import *
import re

game = games.split('\n')

pattern = r'(\d+)\s*([a-zA-Z]+)'

i = 0
res = 0
bool = True

for round in game:
    i += 1
    matches = re.findall(pattern, round)
    numbers_and_colors = [(int(match[0]), match[1]) for match in matches]
    for data in numbers_and_colors:
        if data[0] > 12 and data[1] == "red":
            bool = False
            break
        elif data[0] > 13 and data[1] == "green":
            bool = False
            break
        elif data[0] > 14 and data[1] == "blue":
            bool = False
            break
    if bool == True:
        res += i
    bool = True
print(res)


