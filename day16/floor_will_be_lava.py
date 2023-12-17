import numpy as np, queue as q

lines = open('contraption.txt').read().split('\n')
contraption = np.stack([list(line) for line in lines], dtype = object)

direction_map = {
  '.': {'right': [(0,1,'right')], 'left': [(0,-1,'left')], 'up': [(-1,0,'up')], 'down': [(1,0,'down')]},
  '|': {'right': [(-1,0,'up'),(1,0,'down')], 'left': [(-1,0,'up'),(1,0,'down')], 'up': [(-1,0,'up')], 'down': [(1,0,'down')]},
  '-': {'right': [(0,1,'right')], 'left': [(0,-1,'left')], 'up': [(0,-1,'left'),(0,1,'right')], 'down': [(0,-1,'left'),(0,1,'right')]},
  '\\': {'right': [(1,0,'down')], 'left': [(-1,0,'up')], 'up': [(0,-1,'left')], 'down': [(0,1,'right')]},
  '/': {'right': [(-1,0,'up')], 'left': [(1,0,'down')], 'up': [(0,1,'right')], 'down': [(0,-1,'left')]},
}

def get_next_direction(point, direction):
  if [point, direction] not in visited:
    # this should prevent us from getting caught in a loop by keeping track of the point and the incoming direction
    visited.append([point, direction])
    return direction_map[contraption[point]][direction]
  return []

max_spaces = 0

# i feel like now is the time to start learning memoization
# todo dec 26th or when a problem is too hard to solve brute force
# (lookin at you day 12 part b)
for i in range(len(contraption)-1):
  visited = []
  queue = q.Queue()
  queue.put([(i,len(contraption[0])-1), 'left'])
  while not queue.empty():
    next = queue.get()
    point = next[0]
    direction = next[1]
    steps = get_next_direction(point, direction)
    for step in steps:
      x = point[0] + step[0]
      y = point[1] + step[1]
      if y >=0 and y < len(contraption[0]) and x >= 0 and x < len(contraption):
        queue.put([(x, y), step[2]])

  # convert visited list to include just visited points, convert to set, and count for charged area
  charged_spaces = []
  for point, direction in visited:
    charged_spaces.append(point)
  print(i, len(set(charged_spaces)))
  max_spaces = max(max_spaces, len(set(charged_spaces)))
print(max_spaces)

# 7894 left side
# 9345 right
# 9324 top
# 9091 bottom