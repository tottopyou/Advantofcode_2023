from data import *
import re
import numpy

number = []
res = []

time_numbers = re.findall(r'\b\d+\b', re.search(r'Time:(.*?)Distance:', info, re.DOTALL).group())
distance_numbers = re.findall(r'\b\d+\b', re.search(r'Distance:(.*?)$', info, re.DOTALL).group())

for time, distance in zip(time_numbers, distance_numbers):
    time, distance = int(time), int(distance)
    for i in range(time):
        if i * (time - i) < distance:
            i += 1
        elif i * (time - i) > distance:
            number.append(i)
            i += 1

    res.append(len(number))
    number = []

print(numpy.prod(res))
