def part1(input):
  points = {}
  for line in input:
    p1, p2 = line.strip().split(' -> ')
    x1, y1 = p1.split(',')
    x2, y2 = p2.split(',')
    if x1 == x2:
      dots = get_start_end(int(y1), int(y2))
      for i in dots:
        p = x1 + ';' + str(i)
        if p in points:
          points[p] += 1
        else:
          points[p] = 1
    elif y1 == y2:
      dots = get_start_end(int(x1), int(x2))
      for i in dots:
        p = str(i) + ';' + y1
        if p in points:
          points[p] += 1
        else:
          points[p] = 1
  return len([v for v in points.values() if v > 1])


def part2(input):
  points = {}
  for line in input:
    p1, p2 = line.strip().split(' -> ')
    x1, y1 = p1.split(',')
    x2, y2 = p2.split(',')
    if x1 == x2:
      dots = get_start_end(int(y1), int(y2))
      for i in dots:
        p = x1 + ';' + str(i)
        if p in points:
          points[p] += 1
        else:
          points[p] = 1
    elif y1 == y2:
      dots = get_start_end(int(x1), int(x2))
      for i in dots:
        p = str(i) + ';' + y1
        if p in points:
          points[p] += 1
        else:
          points[p] = 1
    else:
      xdots = get_start_end(int(x1), int(x2))
      ydots = get_start_end(int(y1), int(y2))
      for i in range(len(xdots)):
        p = str(xdots[i]) + ';' + str(ydots[i])
        if p in points:
          points[p] += 1
        else:
          points[p] = 1
  return len([v for v in points.values() if v > 1])


def get_start_end(n1, n2):
  if n1 > n2:
    return [i for i in range(n1, n2 - 1, -1)]
    return n2, n1 + 1
  return [i for i in range(n1, n2 + 1)]
  return n1, n2 + 1


with open('inputs/05.txt', 'r') as f:
  lines = f.readlines()

print(part1(lines))
print(part2(lines))
