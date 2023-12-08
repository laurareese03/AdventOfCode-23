lines = open('hands.txt').readlines()
plays = {
  'five': [],
  'four': [],
  'full': [],
  'three': [],
  'two': [],
  'one': [],
  'high': []
}

bids = {}

# now let's think about this.
# 5 of a kind: set length 1, max count 5
# 4 of a kind: set length 2, max count 4
# full house : set length 2, max count 3
# 3 of a kind: set length 3, max count 3
# 2 pair     : set length 3, max count 2
# 1 pair:    : set length 4, max count 2
# high count : set length 5, max count 1
# this means a hell of a lot of if statements :/

def get_highest_count(hand, cards):
  counts = []
  for card in cards:
    counts.append(hand.count(card))
  return max(counts)

def get_hand_type(line):
  hand = line[0]
  cards = set(hand)

  if len(cards) == 1:
    plays['five'].append(hand)
  elif len(cards) == 2:
    if get_highest_count(hand, cards) == 4:
      plays['four'].append(hand)
    else:
      plays['full'].append(hand)
  elif len(cards) == 3:
    if get_highest_count(hand, cards) == 3:
      plays['three'].append(hand)
    else:
      plays['two'].append(hand)
  elif len(cards) == 4:
    plays['one'].append(hand)
  else:
    plays['high'].append(hand)

# organize the hands into types
for line in lines:
  line = line.split()
  bids[line[0]] = line[1]
  get_hand_type(line)

# go through each type, sort the hands, find the rank, and total
current_rank = len(lines)
total = 0
for play in plays:
  alphabet = "AKQJT98765432"

  # custom sorting per 
  # https://stackoverflow.com/questions/26579392/sorting-string-values-according-to-a-custom-alphabet-in-python 
  sorts = sorted(plays[play], key=lambda word: [alphabet.index(c) for c in word])
  for sort in sorts:
    total += (current_rank * int(bids[sort]))
    current_rank -= 1
print(total)