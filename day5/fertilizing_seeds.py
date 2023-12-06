lines = open('alminac.txt').read()
lines = lines.split('\n')

seeds = [int(x) for x in lines[0][7:].split(' ')]
conversions = []

for i in range(2,len(lines)):
  line = lines[i].split(' ')
  if line[0] == '':
    for j in range(len(seeds)):
      for conversion in conversions:
        if seeds[j] >= conversion[1] and seeds[j] <= conversion[1]+conversion[2]:
          offset = seeds[j] - conversion[1]
          seeds[j] = conversion[0] + offset
          break
    # refigure indexes here
    conversions = []
  else:
    try:
      line = [int(x) for x in line]
      conversions.append(line)
    except:
      holder = 0
  
print(min(seeds))

seeds = lines[0][7:].split(' ')
seed_pairs = [[int(seeds[i]), int(seeds[i+1])] for i in range(0, len(seeds), 2)]
location = 56931750 # approximation from running seed +500000
seed = 56931750
conversions = []
done = False
# we've got to go back! (backwards, that is)
while not done: # god i h8 it here
  for i in range(len(lines)-1, 0, -1):
    line = lines[i].split(' ')
    if line[0] == '':
      for conversion in conversions:
        if location >= conversion[0] and location <= conversion[0]+conversion[2]:
          offset = location - conversion[0]
          location = conversion[1] + offset
          break
      # refigure indexes here
      conversions = []
    else:
      try:
        line = [int(x) for x in line]
        conversions.append(line)
      except:
        holder = 0
  for pair in seed_pairs:
    if location >= pair[0] and location < pair[0]+pair[1]:
      done = True
  seed += 1 # originally ran by +500000 to get close, then narrowed it down to one when it hit a result
  location = seed

print(seed-1)