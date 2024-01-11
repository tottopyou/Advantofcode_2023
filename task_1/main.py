from data import *
import re
def word_to_number(word):
    word_mapping = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    pattern = '|'.join(re.escape(key) for key in word_mapping.keys())
    regex = re.compile(pattern)

    result = regex.sub(lambda match: str(word_mapping[match.group()]), word)
    return result

integer_number = word_to_number(string)

splited_num = integer_number.split()

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