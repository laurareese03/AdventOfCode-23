# "You resume walking through the valley of mirrors and - SMACK! - run directly into one."
# yeah, that's what I'd like to be doing rn

import numpy as np, collections

lines = open('landscape.txt').read().split('\n\n')

def are_smudged(l1, l2):
  equals = l1 == l2
  return len(equals[equals == False]) == 1

count = 0
for line in lines:
  need_columns = True
  passed_columns = False
  smudge_used = False
  rows = [list(i) for i in line.split('\n')]
  grid = np.stack(rows, dtype=object)

  # columns grid[:,i] rows grid[i,:]
  for i in range(len(grid)-1):
    l1 = grid[i,:]
    l2 = grid[i+1,:]
    if (l1 == l2).all() or are_smudged(l1, l2):
      expand_list1 = grid[:i+1][::-1]
      expand_list2 = grid[i+1:]
      attempt = True
      if len(expand_list1) > len(expand_list2):
        holder = expand_list1
        expand_list1 = expand_list2
        expand_list2 = holder
      expand_list2 = expand_list2[:len(expand_list1)]

      if are_smudged(expand_list1, expand_list2):
        count += 100*(i+1)
        need_columns = False
        break

  if need_columns:
    for i in range(len(grid[0])-1):
      l1 = grid[:,i]
      l2 = grid[:,i+1]
      if (l1 == l2).all() or are_smudged(l1, l2):
        expand_list1 = grid[:,i+1:]
        expand_list2 = np.fliplr(grid[:,:i+1])
        if len(expand_list1[0]) > len(expand_list2[0]):
          holder = expand_list1
          expand_list1 = expand_list2
          expand_list2 = holder
        expand_list2 = expand_list2[:,:len(expand_list1[0])]
        attempt = True
        min_val = min(len(expand_list1[0]), len(expand_list2[0]))

        if are_smudged(expand_list1, expand_list2):
          count += i+1
          passed_columns = False
          break
print(count)