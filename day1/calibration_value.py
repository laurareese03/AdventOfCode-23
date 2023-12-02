import regex as re

with open('input.txt') as f:
  lines = f.readlines()

words = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

count_a = 0
count_b = 0
for line in lines:
  pattern = re.findall(r'\d', line)
  pair = int(str(pattern[0]) + str(pattern[-1]))
  count_a += pair

  pattern = re.findall(r'|'.join(words.keys()) + r'|\d', line, overlapped=True)
  pattern = [words[x] if x in words.keys() else x for x in pattern]
  pair = int(str(pattern[0]) + str(pattern[-1]))
  count_b += pair

print(count_a, count_b)