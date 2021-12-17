def part1(input):
  rev = [[int(line[i]) for line in input] for i in range(len(input[0]))]
  gbin = [1 if sum(n) > len(n) // 2 else 0 for n in rev]
  ebin = [1 if n == 0 else 0 for n in gbin]
  return bin_to_dec(gbin) * bin_to_dec(ebin)

def bin_to_dec(input):
  return sum([j * (2**i) for i, j in enumerate(input[::-1])])


def part2(input):
  oxy = get_oxy(input[:])
  co2 = get_co2(input[:])
  return bin_to_dec(oxy) * bin_to_dec(co2)

def get_oxy(input):
  i = 0
  while len(input) > 1:
    bit = '1' if sum([int(line[i]) for line in input]) >= len(input) / 2 else '0'
    input = [line for line in input if line[i] == bit]
    i += 1
  return [int(i) for i in input[0]]

def get_co2(input):
  i = 0
  while len(input) > 1:
    bit = '1' if sum([int(line[i]) for line in input]) >= len(input) / 2 else '0'
    input = [line for line in input if line[i] != bit]
    i += 1
  return [int(i) for i in input[0]]

with open('inputs/03.txt', 'r') as f:
  stuff = [l.strip() for l in f]
print(part1(stuff))
print(part2(stuff))