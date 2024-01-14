from data import *
import re

card_string = games.split('\n')

win_card = []
step = 0.5
res = []

for card in card_string:
    winning_numbers = re.findall(r'\b\d+\b', card.split('|')[0])
    your_numbers = re.findall(r'\b\d+\b', card.split('|')[1])
    winning_numbers.pop(0)
    print("Winning Numbers:", winning_numbers)
    print("Your Numbers:", your_numbers)
    for num in your_numbers:
        if num in winning_numbers:
            win_card.append(num)

    if win_card:
        for win in win_card:
            step *= 2
        res.append(step)
    win_card = []
    step = 0.5

print(sum(res))