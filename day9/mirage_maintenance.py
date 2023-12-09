lines = open('history.txt').read().split('\n')

# algebraic series?
# how do we change d in 
# a_n = a_1 + (n - 1) * d 
# to reflect nested compounding algebraic series?

# recursion!!! yay!!!
# there has to be a nonrecursive solution to this.
# maybe I'll do a little more thinking, or maybe consult reddit
# but either way its quicker to go this way now
def get_next_sequence(sequence):
  if len(set(sequence)) == 1:
    return sequence[0]
  new_sequence = []
  for i in range(len(sequence)-1):
    new_sequence.append(int(sequence[i+1]) - int(sequence[i]))
  return int(sequence[0]) - get_next_sequence(new_sequence)

total = 0
for line in lines:
  total += get_next_sequence(line.split())
print(total)