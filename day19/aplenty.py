import re

lines = open('workflows.txt').read().split('\n\n')

instructions = lines[0].split('\n')
parts = lines[1].split('\n')

def get_part_acceptance(instruction, categories):
  for i in workflow[instruction]:
    category = categories[i['eval'][0]]
    if eval(category + i['eval'][1:]):
      return i['destination']

def get_part_total(categories):
  return int(categories['x']) + int(categories['m']) + int(categories['a']) + int(categories['s'])

workflow = {}
for instruction in instructions:
  flow = re.match(r'\w+', instruction)
  workflow[flow.group()] = []

  instruction_set = re.search(r'{\S+}', instruction)
  instruction_set = instruction_set.group()[1:-1].split(',')
  for i in instruction_set:
    if ':' in i:
      i = i.split(':')
      workflow[flow.group()].append({ 'eval': i[0], 'destination': i[1]})
    else:
      workflow[flow.group()].append({ 'eval': 'True', 'destination': i})

total = 0
for part in parts:
  categories = {'T': 'T'}
  components = part[1:-1].split(',')
  for component in components:
    component = component.split('=')
    categories[component[0]] = component[1]

  part_finished = False
  instruction = 'in'
  while not part_finished:
    instruction = get_part_acceptance(instruction, categories)
    if instruction == 'A':
      total += get_part_total(categories)
      break
    elif instruction == 'R':
      break
print(total)