import numpy as np, collections

lines = open('landscape.txt').read().split('\n\n')

count = 0
for line in lines:
  print('____________')
  print(line)
  need_columns = True
  passed_columns = False
  smudge_used = False
  rows = [list(i) for i in line.split('\n')]
  grid = np.stack(rows, dtype=object)

  # columns grid[:,i] rows grid[i,:]
  for i in range(len(grid)-1):
    l1 = str(grid[i,:])
    l2 = str(grid[i+1,:])
    if l1 == l2:
      expand_list1 = grid[:i+1][::-1]
      expand_list2 = grid[i+1:]
      attempt = True
      if len(expand_list1) > len(expand_list2):
        holder = expand_list1
        expand_list1 = expand_list2
        expand_list2 = holder
      # print(expand_list1)
      # print(expand_list2)
      for j in range(len(expand_list1)):
        # print(expand_list1[j], expand_list2[j])
        if str(expand_list1[j]) != str(expand_list2[j]):
          attempt = False
      if attempt and smudge_used:
        count += 100*(i+1)
        print('row', i+1)
        need_columns = False
        break

  if need_columns:
    for i in range(len(grid[0])-1):
      l1 = str(grid[:,i])
      l2 = str(grid[:,i+1])
      print(l1, l2)
      if l1 == l2:
        expand_list1 = grid[:,i+1:]
        expand_list2 = np.fliplr(grid[:,:i+1])
        if len(expand_list1[0]) > len(expand_list2[0]):
          holder = expand_list1
          expand_list1 = expand_list2
          expand_list2 = holder
        print(expand_list1)
        print(expand_list2)
        attempt = True
        min_val = min(len(expand_list1[0]), len(expand_list2[0]))
        for j in range(min_val):
          # print(str(expand_list1[:,j]), str(expand_list2[:,len(expand_list2[0])-1-j]))
          # print(str(expand_list1[:,j]) != str(expand_list2[:,len(expand_list2[0])-1-j]))
          if str(expand_list1[:,j]) != str(expand_list2[:,j]):
            attempt = False
            # print(j)
        if attempt and smudge_used:
          count += (i+1)
          print('column', i+1)
          passed_columns = True
          break
    if not passed_columns:
      input()
  print(count)
print(count)

# 34122 low
# 26849 low
# + 7