import re

lines = open('network.txt').read().split('\n')

directions = lines.pop(0).replace('L', '0').replace('R', '1')
lines.pop(0)

network = {}
# build the network!
for line in lines:
  pattern = re.compile(r'[A-Z]{3}')
  nodes = re.findall(pattern, line)
  network[nodes[0]] = [nodes[1], nodes[2]]

# recursion!!! no!!!
count = 0
node = 'AAA'
while node != 'ZZZ':
  node = network[node][int(directions[count % len(directions)])]
  count += 1

print(count)