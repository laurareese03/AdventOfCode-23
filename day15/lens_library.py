lines = open('initialization_sequence.txt').read().split(',')

def get_hash_output(str):
  result = 0
  for char in list(str):
    result += ord(char)
    result *= 17
    result %= 256
  return result

total = 0
for line in lines:
  result = get_hash_output(line)
  total += result
print(total)