import re

lines = open('engine_schematic.txt').readlines()

symbol_positions = set()
# compile a set of all indexes of characters
for i in range(len(lines)):
  line = lines[i].strip()
  symbol_list = re.finditer(r'([^\w|\.|\s])', line) # non period, non alphanumeric, non whitespace

  for symbol in symbol_list:
    symbol_positions.add((symbol.start(1), i))

total = 0
# compile set of indexes surrounding each number :))))))
for i in range(len(lines)):
  line = lines[i].strip()
  number_list = re.finditer(r'\d+', line)

  for number in number_list:
    number_edge_positions = set()
    [number_edge_positions.add((j, k)) for j, k in ((j, k) for j in range(number.start()-1, number.end()+1) for k in range(i-1, i+2))]
    u = number_edge_positions.intersection(symbol_positions)
    if len(u) > 0:
      total += int(number.group())

print(total)