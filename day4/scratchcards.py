import re, itertools

lines = open('scores.txt').readlines()

def get_set_intersects(line):
  line = line.split(':')[1].split('|')
  pattern = re.compile('\d+')
  card_nums = set(re.findall(pattern, line[0]))
  winning_nums = set(re.findall(pattern, line[1]))
  return len(card_nums.intersection(winning_nums))

# part a
worth = 0
for line in lines:
  card_wins = get_set_intersects(line)
  if card_wins: worth += (2 ** (card_wins - 1))
print(worth)

# part b
total_cards = 0
card_multiples = [1] * len(lines) # stores how many of each future card we have. start with 1 og, with more to be
for line in lines:
  current_cards = card_multiples.pop(0)
  # for each original card, we have to add the number of current card duplicates to our total
  total_cards += current_cards
  # for each duplicate card we have we have to add multiples of [matching numbers (intersect)] number of future cards
  card_wins = get_set_intersects(line)
  added_cards = [current_cards] * card_wins
  card_multiples = [i+j for i,j in itertools.zip_longest(card_multiples, added_cards,fillvalue = 0)]
print(total_cards)