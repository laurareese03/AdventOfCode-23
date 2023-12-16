lines = open('initialization_sequence.txt').read().split(',')

def get_hash_output(str):
  result = 0
  for char in list(str):
    result += ord(char)
    result *= 17
    result %= 256
  return result

boxes = [{}.copy() for i in range(256)]
for line in lines:
  if line[-1] != '-':
    line = line.split('=')
    result = get_hash_output(line[0])
    boxes[result][line[0]] = line[1]
  else:
    box = get_hash_output(line[:-1])
    try:
      del boxes[box][line[:-1]]
    except:
      here = True

focusing_power = 0
for i in range(len(boxes)):
  slot = 1
  for lens in boxes[i]:
    focusing_power += (i+1) * slot * int(boxes[i][lens])
    slot += 1
print(focusing_power)