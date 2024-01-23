from data import *
import numpy as np

matrix = np.array([list(row) for row in space.split('\n')])
hashes = [(i, j) for i, row in enumerate(matrix) for j, char in enumerate(row) if char == '#']

print(matrix)


distance = []
sorted_hashes = sorted(hashes, key=lambda x: x[1])
print(sorted_hashes )

for mark in sorted_hashes:
    for rev_mark in reversed(sorted_hashes):
        if sum(rev_mark) - sum(mark) > 0:
            distance.append(sum(rev_mark) - sum(mark))
            print(distance)

print(sum(distance))