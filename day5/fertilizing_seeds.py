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