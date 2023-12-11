import numpy as np, math

lines = open('map.txt').readlines()

str_arr = [list(line.strip()) for line in lines]
arr = np.stack(str_arr, dtype=object)

directions = {
  '|': {'south': [1,0, 'south'], 'north': [-1,0, 'north']},
  '-': {'west': [0,-1, 'west'], 'east': [0,1, 'east']},
  'L': {'west': [-1,0, 'north'], 'south': [0,1, 'east']},
  'J': {'south': [0,-1, 'west'], 'east': [-1,0, 'north']},
  '7': {'north': [0,-1, 'west'], 'east': [1,0, 'south']},
  'F': {'west': [1,0, 'south'], 'north': [0,1, 'east']}
}

# Find the starting point, traverse in one direction adding each point to the map list (maze)
# once we return to the start point, find len(maze)/2 to get furthest point
maze = []
start = np.where(arr == 'S')
maze.append([start[0][0],start[1][0]])
# I usually try and generalize the solution to account for any input, but for this one, we're just gonna start
# one south of S because I can't think of a good way to figure it out in a timely manner
# todo dec 26th
point = [start[0][0]+1,start[1][0]]
cardinal_direction = 'south'

while arr[point[0], point[1]] != 'S':
  direction = directions[arr[point[0],point[1]]][cardinal_direction]
  point = [point[0] + direction[0], point[1] + direction[1]]
  maze.append(point)
  cardinal_direction = direction[2]

print(round(len(maze)/2))