import numpy as np, math
lines = open('galaxies.txt').read().split('\n')

str_arr = [list(line.strip()) for line in lines]
galaxies = np.stack(str_arr, dtype=object)

def get_manhattan_distance(point1, point2):
  return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

empty_rows = []
empty_columns = []
for i in range(galaxies.shape[0]-1, 0, -1):
  if len(set(galaxies[i,:])) == 1:
    inserts = np.full((galaxies.shape[1],), '.', dtype=object)
    galaxies = np.insert(galaxies, i, inserts, axis=0)
    empty_rows.append(i)
for j in range(galaxies.shape[1]-1, 0, -1):
  if len(set(galaxies[:,j])) == 1:
    inserts = np.full((galaxies.shape[0]), '.', dtype=object)
    galaxies = np.insert(galaxies, j, inserts, axis=1)
    empty_columns.append(j)

galaxies = np.where(galaxies == '#')
galaxies = list(zip(galaxies[0], galaxies[1]))

total = 0

# nested for loops! oof!
for i in range(len(galaxies)):
  for j in range(i+1, len(galaxies)):
    md = get_manhattan_distance(galaxies[i], galaxies[j])
    total += get_manhattan_distance(galaxies[i], galaxies[j])
print(total)