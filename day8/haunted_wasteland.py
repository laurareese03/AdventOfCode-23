import re
from math import gcd

readed = open('network.txt').read()
lines = readed.split('\n')

directions = lines.pop(0).replace('L', '0').replace('R', '1')
lines.pop(0)

# some part b questions to ponder
# do they end up at different nodes by the end? or will 2 A nodes map to the same Z node?

# there is a (potentially) clever solution to figure out how each node loops and find the lcm between all of them
# based on how long the LR string is I'm guessing that's not as clever as I think it is
# we're gonna try the option that matches with the part a code first tbh

# hey @ past laura! the idea WAS clever! brute forcing sucks!

network = {}
# build the network!
for line in lines:
  pattern = re.compile(r'[A-Z]{3}')
  nodes = re.findall(pattern, line)
  network[nodes[0]] = [nodes[1], nodes[2]]

# recursion!!! no!!!
node_list = re.findall(r'[A-Z]{2}A', readed)
counts = []
for node in node_list:
  count = 0
  while node[-1] != 'Z':
    node = network[node][int(directions[count % len(directions)])]
    count += 1
  # VERY fortunate that the first time we get to a node ending in Z, the complete cycle repeats
  counts.append(count)

# least common multiple for n inputs from
# https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
lcm = 1
for i in counts:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)