def part1(input):
  hor = 0
  dep = 0
  for dir, val in input:
    if dir == 'forward':
      hor += val
    elif dir == 'up':
      dep -= val
    elif dir == 'down':
      dep += val
  return hor*dep


def part2(input):
  hor = 0
  dep = 0
  aim = 0
  for dir, val in input:
    if dir == 'forward':
      hor += val
      dep += aim * val
    if dir == 'up':
      aim -= val
    if dir == 'down':
      aim += val
  return hor*dep


with open('inputs/02.txt', 'r') as f:
  stuff = []
  for line in f:
    d, s = line.split()
    stuff.append((d, int(s)))

print(part1(stuff))
print(part2(stuff))
