import itertools, re

lines = open('spring_conditions.txt').read().split('\n')

def convert_to_string(bools):
  return ['#' if bool else '.' for bool in bools]

# forget it im brute forcing
valid_count = 0
for line in lines:
  print(line)
  line = line.split(' ')

  # what we'll validate our tests against
  check_list = [int(i) for i in str(line[1]).split(',')]

  springs = [i.span() for i in re.finditer('\?', line[0])]
  for i in range(2**len(springs)):
    # https://stackoverflow.com/questions/33608280/convert-4-bit-integer-into-boolean-list
    bool_list = [bool(i & (1<<n)) for n in range(len(springs))]
    bool_list = convert_to_string(bool_list)
    
    test_string = line[0]
    for i in range(len(springs)):
      test_string = test_string[:springs[i][0]] + bool_list[i] + test_string[springs[i][0] + 1:]
    test_list = [len(i) for i in re.findall('#+', test_string)]
    if test_list == check_list:
      valid_count += 1

print(valid_count)

# right now, this code checks ALL possible ./# combinations to replace ?
# however, we know that we should have exactly the same number of springs as given in the spring condition
# this would cut the amount of time for this brute force considerably, but I don't think its gonna be helpful
# for part b. 
# leaving it for todo dec 26th