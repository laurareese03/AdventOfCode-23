import re

with open('game_results.txt') as f:
  lines = f.readlines()

maxes = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

# MORE regexes?? in this economy?? more likely than you think
valid_games = 0
game_num = 0
total = 0
for line in lines:
  game_is_valid = True
  game_num += 1
  power = 1

  for color in maxes:
    pattern = re.compile = (r'\d+(?= ' + color + r')')
    selections = [int(x) for x in re.findall(pattern, line)]

    # part a work
    if any(i > maxes[color] for i in selections):
      game_is_valid = False

    if color == 'blue' and game_is_valid:
      valid_games += game_num

    # part b work
    max_val = max(selections)
    power *= max_val 

  total += power

print(valid_games, total) # part a, part b