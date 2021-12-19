import math

def part1(input):
  rl = 0
  for i in range(len(input)):
    for j in range(len(input[i])):
      lp = chk_adj(i, j, input)
      rl += lp + 1 if lp is not None else 0
  return rl

def part2(input):
  basins = []
  for i in range(len(input)):
    for j in range(len(input[i])):
      lp = chk_adj(i, j, input)
      if lp is not None:
        basin = travel(i, j, input)
        basins.append(len(basin))
  return math.prod(sorted(basins)[-3:])

def travel(i,j,input,p=None):
  if p is None:
    p = set()
  point = f'{i}:{j}'
  if input[i][j] == '9' or point in p:
    return p
  p.add(point)
  if i > 0:
    up = travel(i-1, j, input, p)
    [p.add(n) for n in up]
  if j > 0:
    left = travel(i, j-1, input, p)
    [p.add(n) for n in left]
  try:
    _ = input[i+1][j]
    down = travel(i+1, j, input, p)
    [p.add(n) for n in down]
  except:
    pass
  try:
    _ = input[i][j+1]
    right = travel(i, j+1, input, p)
    [p.add(n) for n in right]
  except:
    pass
  return p

def chk_adj(i,j,input):
  current = int(input[i][j])
  if i > 0:
    above = int(input[i-1][j])
    if above <= current:
      return
  try:
    below = int(input[i+1][j])
    if below <= current:
      return
  except:
    pass
  if j > 0:
    left = int(input[i][j-1])
    if left <= current:
      return
  try:
    right = int(input[i][j+1])
    if right <= current:
      return
  except:
    pass
  return current


filename = 'inputs/09-test.txt'
filename = 'inputs/09.txt'
with open(filename, 'r') as f:
  stuff = f.readlines()

print(part1([l.strip() for l in stuff]))
print(part2([l.strip() for l in stuff]))
