import re

with open('game_results.txt') as f:
  lines = f.readlines()

games = {}
maxes = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

# MORE regexes?? in this economy?? more likely than you think
valid_games = 0
game_num = 0
for line in lines:
  game_num += 1
  for color in maxes:
    pattern = re.compile = (r'\d+(?= ' + color + r')')
    selections = [int(x) for x in re.findall(pattern, line)]
    total = sum(selections)

    if any(i > maxes[color] for i in selections):
      break

    if color == 'blue':
      valid_games += game_num

print(valid_games)