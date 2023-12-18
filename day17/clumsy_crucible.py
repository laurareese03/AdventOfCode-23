import numpy as np, queue

lines = open('heat_loss.txt').read().split('\n')
lines = np.stack([list(line) for line in lines])

def is_real(point_info):
  node = point_info[0]
  direction_length = point_info[1]
  return direction_length < 4 and (node[0] >= 0) and (node[0] < len(lines)) and (node[1] >= 0) and (node[1] < len(lines[0])) and node not in visited

frontier = queue.PriorityQueue()
frontier.put((0, [(0,0), 'left', 0])) # top left corner
visited = []

while not frontier.empty():
  node = frontier.get()
  input = node[1]
  point = input[0]
  if node in visited:
    print('HERE', node)
    continue
  visited.append(node)
  if point == (len(lines)-1, len(lines[0])-1):
    print(node[0], 'HERE')
    break
  print(node)
  last_direction = input[2]
  direction_length = input[1]
  new_nodes = []
  new_nodes.append([(point[0]-1, point[1]), 1, 'up'])
  new_nodes.append([(point[0], point[1]+1), 1, 'right'])
  new_nodes.append([(point[0]+1, point[1]), 1, 'down'])
  new_nodes.append([(point[0], point[1]-1), 1, 'left'])

  for i in range(len(new_nodes)-1, -1, -1):
    if new_nodes[i][2] == last_direction:
      new_nodes[i] = [new_nodes[i][0], direction_length + 1, last_direction]
    if is_real(new_nodes[i]):
      print((node[0]+ int(lines[new_nodes[i][0]]), new_nodes[i]))
      frontier.put((node[0]+ int(lines[new_nodes[i][0]]), new_nodes[i]))

# 1066 high