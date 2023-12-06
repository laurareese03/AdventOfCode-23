import re, math

lines = open('races.txt').readlines()
pairs = []
pairs = [re.findall(r'\d+', lines[0]), re.findall(r'\d+', lines[1])]

str1 = ''
str2 = ''
for num in pairs[0]:
  str1 += num
for num in pairs[1]:
  str2 += num
pairs = [[str1], [str2]]

# quadratic formula aw yea
# we're assuming all races have at least 1 way to win. If not, answer would be 0, which is no fun
def get_roots(distance, time):
  return (time - math.sqrt((time**2) - (4*distance)))/2, (time + math.sqrt((time**2) - (4*distance)))/2

options = 1
for i in range(len(pairs[0])):
  min, max = get_roots(int(pairs[1][i]), int(pairs[0][i]))
  diff = math.floor(max - .01) - math.ceil(min + .01) + 1
  print(diff)
  options *= diff
print(options)