def part1(input):
  min_line = 0
  max_line = max(input)
  while max_line - min_line > 1:
    mid = (max_line - min_line) // 2 + min_line
    lower = sum([abs(n - mid) for n in input])
    higher = sum([abs(n - (mid + 1)) for n in input])
    if (lower > higher):
      min_line = mid + 1
      mid += 1
    else:
      max_line = mid
  return sum([abs(n - mid) for n in input])

def part2(input):
  min_line = 0
  max_line = max(input)
  lowest = 100**1000
  steps = {i : sum([n for n in range(i+1)]) for i in range(max_line+1)}
  while max_line - min_line > 1:
    mid = (max_line - min_line) // 2 + min_line
    lower = sum([steps[abs(n-mid)] for n in input])
    higher = sum([steps[abs(n-(mid+1))] for n in input])
    if (lower > higher):
      min_line = mid + 1
      mid += 1
      if higher < lowest:
        lowest = higher
    else:
      max_line = mid
      if lower < lowest:
        lowest = lower
  return lowest


filename = 'inputs/07-test.txt'
filename = 'inputs/07.txt'
with open(filename, 'r') as f:
  stuff = f.readline()

print(part1([int(n) for n in stuff.strip().split(',')]))
print(part2([int(n) for n in stuff.strip().split(',')]))
