import numpy as np

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
maze.append(point)
cardinal_direction = 'south'

while arr[point[0], point[1]] != 'S':
  direction = directions[arr[point[0],point[1]]][cardinal_direction]
  point = [point[0] + direction[0], point[1] + direction[1]]
  maze.append(point)
  cardinal_direction = direction[2]

num_points = int((len(maze)-1)/2)
print(num_points)

# pretty pictures
pipe = np.full((len(lines),len(lines[0])), ' ', dtype=object)
for i,j in maze:
  pipe[i, j] = arr[i,j]
np.savetxt('notes.txt', pipe, fmt='%s', delimiter='')

# shoelace!!! it all comes full circle!
double_area = 0
for i in range(len(maze)-1):
  matrix = np.stack([maze[i], maze[i+1]], dtype=int)
  double_area += np.linalg.det(matrix)
double_area = round(abs(double_area/2))

# pick's theorem! (assuming no holes)
# A=i+b/2-1
interior_points = double_area - num_points + 1
print(interior_points)

# [x, y+1] and follow
# less than 624