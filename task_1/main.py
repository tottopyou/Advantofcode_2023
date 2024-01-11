from data import *

splited_num = string.split()

array = []
result_arr = []
symbol = 0

for str in splited_num:
    for symbol in str:
        if symbol.isdigit():
            array.append(symbol)
    if len(array) == 1:
        symbol = array[0] * 2
        result_arr.append(int(symbol))
        array = []
    elif len(array) > 1:
        symbol = array[0] + array[-1]
        result_arr.append(int(symbol))
        array = []

print(sum(result_arr))