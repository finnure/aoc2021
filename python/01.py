def part1(input):
  last = 0
  inc = -1
  for line in input:
    curr = line
    if curr > last:
      inc += 1
    last = curr
  return inc

def part2(input):
  last = sum(input[0:3])
  inc = 0
  for i in range(1, len(input) -2):
    curr = sum(input[i:i+3])
    if curr > last:
      inc += 1
    last = curr
  return inc



with open('inputs/01.txt', 'r') as f:
  stuff = [int(l) for l in f]
  print(part1(stuff))
  print(part2(stuff))

