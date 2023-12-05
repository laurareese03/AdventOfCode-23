import re

lines = open('scores.txt').readlines()

worth = 0
for line in lines:
  line = line.split(':')[1].split('|')
  pattern = re.compile('\d+') # 'Card \d+: (\d+)*\|(\d+)'
  card_nums = set(re.findall(pattern, line[0]))
  winning_nums = set(re.findall(pattern, line[1]))
  card_wins = len(card_nums.intersection(winning_nums))
  if card_wins:
    worth += (2** (card_wins - 1))

print(worth)