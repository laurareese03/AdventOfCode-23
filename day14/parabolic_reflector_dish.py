import numpy as np, re

lines = open('platform.txt').read().split('\n')
platform = np.stack([list(line) for line in lines], dtype=object)

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

# count the rocks!
total_weight = 0
for i in range(len(platform)):
  row_count = np.char.count(np.array_str(platform[i,:]), 'O')
  total_weight += row_count * (len(platform)-i)
print(total_weight)