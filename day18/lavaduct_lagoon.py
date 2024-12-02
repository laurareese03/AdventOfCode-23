import numpy as np, queue

lines = open('dig_plan.txt').read().split('\n')

points = [(0,0)]
perimeter = 0
for line in lines:
  line = line.split(' ')
  distance = int(line[1])
  next_point = ()
  for i in range(distance):
    last_point = points[-1]
    if line[0] == 'D':
      next_point = (last_point[0]+1, last_point[1])
    elif line[0] == 'L':
      next_point = (last_point[0], last_point[1]-1)
    elif line[0] == 'U':
      next_point = (last_point[0]-1, last_point[1])
    else: # line[0] == 'R'
      next_point = (last_point[0], last_point[1]+1)
    points.append(next_point)

# # flood fill :|
frontier = queue.Queue()
frontier.put((-1,-1))
while not frontier.empty():
  point = frontier.get()
  if point in points:
    continue
  points.append(point)
  frontier.put((point[0]+1, point[1]))
  frontier.put((point[0], point[1]+1))
  frontier.put((point[0]-1, point[1]))
  frontier.put((point[0], point[1]-1))
print(len(set(points)))

points = [(0,0)]
directions = ['R', 'D', 'L', 'U']
perimeter = 0
for line in lines:
  line = line.split(' ')[2]
  distance = int(line[2:-2], 16)
  direction = directions[int(line[-2])]
  last_point = points[-1]
  new_point = ()
  if direction == 'R':
    new_point = (last_point[0], last_point[1]+distance)
  elif direction == 'U':
    new_point = (last_point[0]-distance, last_point[1])
  elif direction == 'L':
    new_point = (last_point[0], last_point[1]-distance)
  else: # direction == 'D'
    new_point = (last_point[0]+distance, last_point[1])
  perimeter += distance
  points.append(new_point)

# weird combo of pick's & shoelace
# find the area using shoelace, and use that to calculate number of interior points using pick's
# add interior points to perimeter to get total volume
total = 0
for i in range(len(points)-1):
  total += np.linalg.det((points[i], points[i+1]))

area = round(abs(total)/2) # can't use int() here! learned the hard way!
interior_points = (area + 1) - int(perimeter/2)
print(interior_points + perimeter)