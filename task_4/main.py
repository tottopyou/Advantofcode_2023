from data import *
import re

card_string = games.split('\n')

win_card = []
res = []
game = {}
copy_list = []

for card in card_string:
    winning_numbers = re.findall(r'\b\d+\b', card.split('|')[0])
    your_numbers = re.findall(r'\b\d+\b', card.split('|')[1])
    game[winning_numbers[0]] = 1


for i, card in enumerate(card_string):
    winning_numbers = re.findall(r'\b\d+\b', card.split('|')[0])
    your_numbers = re.findall(r'\b\d+\b', card.split('|')[1])
    winning_numbers.pop(0)

    for num in your_numbers:
        if num in winning_numbers:
            win_card.append(num)

    if win_card:
        for win in win_card:
            for _ in range(game[str(i+1)]):
                copy_list.append(str(i+2))
            i += 1

    for copy in copy_list:
        game[copy] += 1

    copy_list = []
    win_card = []
print(game)
print(sum(game.values()))