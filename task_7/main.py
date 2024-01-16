from data import *
import re
from collections import Counter

pattern = re.compile(r'(\w+) (\d+)')

symbols = []
result_dict = {}
dict_b = {}
score = []


matches = re.findall(pattern, info)
for match in matches:
    key, value = match
    str_to_list = key
    for symbol in str_to_list:
        symbol = symbol.replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')
        symbols.append(symbol)
    a = Counter(symbols)

    while True:
        max_symbol = max(symbols)
        score.append(int(max_symbol) * a[max_symbol])

        if list(a.values()).count(a[max_symbol]) > 1:
            del a[max_symbol]
        else:
            break

    dict_b[str(key)] = sum(score)

    symbols = []

    result_dict[key] = int(value)

    print(result_dict)
    print(dict_b)
