from data import *

per = matrix.split()
def get_neighbours(data, cell):

    row, col = cell[0], cell[1]
    row_max = len(data)
    col_max = len(data[0])

    return [data[row_d + row][col_d + col]
            for col_d in [-1, 0, 1]
            if (0 <= (col_d + col) < col_max) or (col_d == 0 and row_d == 0)
            for row_d in [-1, 0, 1]
            if 0 <= (row_d + row) < row_max]

print(per)
number = []
bool_res = []
result = []
numbers = []



for i, line in enumerate(per):
    for j, symbol in enumerate(line):
        if symbol.isdigit():
            number.append(symbol)
            neighbours = get_neighbours(per,[i,j])
            if '*' in neighbours:
                bool_res.append(True)
            else:
                bool_res.append(False)
        elif not symbol.isdigit():
            res_number =''.join(number)
            if True in bool_res:
                result.append(int(res_number))
                number = []
                bool_res = []
            else:
                number = []
                bool_res = []

print(result)