from data import *
import re

game = games.split('\n')

pattern = r'(\d+)\s*([a-zA-Z]+)'

res = []
power_set = 0
red_ar,blue_ar,green_ar = [],[],[]

for round in game:
    matches = re.findall(pattern, round)
    numbers_and_colors = [(int(match[0]), match[1]) for match in matches]
    for data in numbers_and_colors:
        if data[1] == "red":
            red_ar.append(data[0])
        elif data[1] == "green":
            green_ar.append(data[0])
        elif data[1] == "blue":
            blue_ar.append(data[0])
    power_set = max(green_ar) * max(red_ar) * max(blue_ar)
    red_ar, blue_ar, green_ar = [], [], []
    res.append(power_set)

print(sum(res))


