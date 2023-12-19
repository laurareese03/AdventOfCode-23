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

x_min=0
y_min=0
x_max=0
y_max=0
for point in points:
  x_min = min(x_min, point[0])
  y_min = min(y_min, point[1])
  x_max = max(x_max, point[0])
  y_max = max(y_max, point[1])
print(x_min, y_min, x_max, y_max)

# flood fill :|
frontier = queue.Queue()
frontier.put((-1,-1))
while not frontier.empty():
  point = frontier.get()
  print(point)
  if point in points:
    print('here?', len(points))
    continue
  points.append(point)
  frontier.put((point[0]+1, point[1]))
  frontier.put((point[0], point[1]+1))
  frontier.put((point[0]-1, point[1]))
  frontier.put((point[0], point[1]-1))

print(points)

print(len(set(points)))