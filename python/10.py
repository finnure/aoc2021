o = '([{<'
c = ')]}>'
p = [3, 57, 1197, 25137]

def part1(input):
  total = 0
  for line in input:
    exp = []
    for t in line:
      if t in o:
        exp.append(c[o.index(t)])
      else:
        if t != exp.pop():
          total += p[c.index(t)]
          break
  return total


def part2(input):
  scores = []
  for line in input:
    exp = []
    corrupt = False
    for t in line:
      if t in o:
        exp.append(c[o.index(t)])
      else:
        if t != exp.pop():
          corrupt = True
    if not corrupt:
      scores.append(complete(exp))
  return sorted(scores)[len(scores) // 2]

def complete(ends):
  p = [1, 2, 3, 4]
  total = 0
  while len(ends) > 0:
    total *= 5
    total += p[c.index(ends.pop())]
  return total
    

filename = 'inputs/10-test.txt'
filename = 'inputs/10.txt'
with open(filename, 'r') as f:
  stuff = f.readlines()

print(part1([l.strip() for l in stuff]))
print(part2([l.strip() for l in stuff]))
