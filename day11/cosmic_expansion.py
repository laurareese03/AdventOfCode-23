import numpy as np, math
lines = open('galaxies.txt').read().split('\n')

str_arr = [list(line.strip()) for line in lines]
galaxies = np.stack(str_arr, dtype=object)

galaxy_distance = 999999
empty_rows = []
empty_columns = []

def get_manhattan_distance(point1, point2):
  x_diff = abs(point1[0]-point2[0])
  y_diff = abs(point1[1]-point2[1])
  x = [point1[0], point2[0]]
  y = [point1[1], point2[1]]
  x_overlap = len(set(range(min(x), max(x))).intersection(set(empty_rows)))
  y_overlap = len(set(range(min(y), max(y))).intersection(set(empty_columns)))
  return x_diff + y_diff + (x_overlap + y_overlap) * galaxy_distance

for i in range(galaxies.shape[0]-1, 0, -1):
  if len(set(galaxies[i,:])) == 1:
    empty_rows.append(i)
for j in range(galaxies.shape[1]-1, 0, -1):
  if len(set(galaxies[:,j])) == 1:
    empty_columns.append(j)

galaxies = np.where(galaxies == '#')
galaxies = list(zip(galaxies[0], galaxies[1]))

total = 0
# nested for loops! oof!
for i in range(len(galaxies)):
  for j in range(i+1, len(galaxies)):
    md = get_manhattan_distance(galaxies[i], galaxies[j])
    total += md
print(total)