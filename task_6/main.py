from data import *
import re

number = []
res = []

time_info = re.search(r'Time:\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)', info)
distance_info = re.search(r'Distance:\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)', info)

time_numbers = ''.join(time_info.groups())
distance_numbers = ''.join(distance_info.groups())

time, distance = int(time_numbers), int(distance_numbers)
for i in range(time):
    if i * (time - i) < distance:
        i += 1
    elif i * (time - i) > distance:
        number.append(i)
        i += 1

print(len(number))


