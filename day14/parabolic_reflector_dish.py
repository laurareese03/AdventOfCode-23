import numpy as np, re

lines = open('platform.txt').read().split('\n')
platform = np.stack([list(line) for line in lines], dtype=object)

for l in range(500):
  # complete 4 turns, 1 cycle
  for k in range(4):
    # shift the rocks!
    for j in range(len(platform[0])):
      column_string = ''.join(str(x) for x in platform[:,j])
      rocks = column_string.split('#')
      
      for i in range(len(rocks)):
        rocks[i] = list(rocks[i])
        rocks[i].sort(reverse=True)
        rocks[i] = ''.join(str(x) for x in rocks[i])
      column_string = '#'.join(str(rock) for rock in rocks)
      platform[:,j] = list(column_string)
    platform = np.rot90(platform, axes=(1,0))

  # count the rocks!
  total_weight = 0
  for i in range(len(platform)):
    row_count = np.char.count(np.array_str(platform[i,:]), 'O')
    total_weight += row_count * (len(platform)-i)
  print(total_weight)
print(total_weight)

# pattern repeating problem!
# takes FAR too long to brute force, but eventually the platform stablizes after a certain number of cycles
# we let the program run for a little while to figure out the pattern in platform weights
# once we have the pattern, we take (wanted number of cycles - number of pre-stable cycles) % cycle pattern length.
# the answer for this gives us the index in the pattern which contains the weight for the billionth cycle :D