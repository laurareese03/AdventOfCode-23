lines = open('history.txt').read().split('\n')

# algebraic series?
# how do we change d in 
# a_n = a_1 + (n - 1) * d 
# to reflect nested compounding algebraic series?

# recursion!!! yay!!!
def get_next_sequence(sequence):
  print(sequence)
  if len(set(sequence)) == 1:
    return sequence[-1]
  new_sequence = []
  for i in range(len(sequence)-1):
    new_sequence.append(int(sequence[i+1]) - int(sequence[i]))
  return int(sequence[-1]) + get_next_sequence(new_sequence)

total = 0
for line in lines:
  total += get_next_sequence(line.split())
print(total)

# 11865661 low