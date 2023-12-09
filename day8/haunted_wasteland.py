import re

readed = open('network.txt').read()
lines = readed.split('\n')

directions = lines.pop(0).replace('L', '0').replace('R', '1')
lines.pop(0)

# some part b questions to ponder
# do they end up at different nodes by the end? or will 2 A nodes map to the same Z node?

# there is a (potentially) clever solution to figure out how each node loops and find the lcd between all of them
# based on how long the LR string is I'm guessing that's not as clever as I think it is
# we're gonna try the option that matches with the part a code first tbh

# build the network!
network = {}
for line in lines:
  pattern = re.compile(r'[A-Z]{3}')
  nodes = re.findall(pattern, line)
  network[nodes[0]] = [nodes[1], nodes[2]]

# will return true if all nodes end in Z
def evaluate_nodes(list):
  for n in list:
    if n[-1] != 'Z':
      return False
  return True

# recursion!!! no!!!
count = 0
node_list = re.findall(r'[A-Z]{2}A', readed)
while not evaluate_nodes(node_list):
  node_list = [network[node][int(directions[count % len(directions)])] for node in node_list]
  count += 1
  if count % 10000 == 0:
    print(count)

print(count)