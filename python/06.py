def part1(input):
  states = [[], [], [], [], [], [], [], [], []]
  for i in input:
    states[int(i)].append(1)
  for i in range(80):
    rep = states.pop(0)
    states.append(rep)
    states[6].extend(rep)
  return sum([sum(n) for n in states])

def part2(input):
  states = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  for i in input:
    states[int(i)] += 1
  for i in range(256):
    rep = states.pop(0)
    states.append(rep)
    states[6] += rep
  return sum(states)


with open('inputs/06.txt', 'r') as f:
  stuff = f.readline()

print(part1(stuff.strip().split(',')))
print(part2(stuff.strip().split(',')))
