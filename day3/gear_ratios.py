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

gear_positions = set()
ratio_total = 0
# get indexes of all potental gears (*)
for i in range(len(lines)):
  line = lines[i].strip()
  gear_list = re.finditer(r'\*', line)

  for gear in gear_list:
    tangent_numbers = []
    gear_positions.add((gear.start(), i))

    for j in range(i-1, i+2):
      # this BAD, bc lines[-1] would cause issues, but theres no * in the first/last lines so its fine, but bad practice
      # but I'm lazy and would like to have this solved lol
      number_list = re.finditer(r'\d+', lines[j])

      for number in number_list:
        number_edge_positions = set()
        [number_edge_positions.add((j, k)) for j, k in ((j, k) for j in range(number.start()-1, number.end()+1) for k in range(i-1, i+2))]
        # print(number_edge_positions, (gear.start(), i))
        if (gear.start(), i) in number_edge_positions:
          tangent_numbers.append(number.group())
      
    if len(tangent_numbers) == 2:
      ratio_total += int(tangent_numbers[0]) * int(tangent_numbers[1])

print(ratio_total)