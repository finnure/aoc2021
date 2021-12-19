def part1(input):
  uni = 0
  for line in input:
    _, read = line.strip().split(' | ')
    count = [1 for s in read.split() if len(s) < 5 or len(s) == 7]
    uni += sum(count)
  return uni


def part2(input):
  total = 0
  for line in input:
    numbers, readings = line.strip().split(' | ')
    decoded = decode_wires(sorted(numbers.split(), key=len))
    total += get_value(decoded, readings.split())
  return total

def get_value(decoded, readings):
  digits = ''
  for digit in readings:
    digits += str(decoded[''.join(sorted(list(digit)))])
  return int(digits)

def compare(big, small):
  for c in small:
    if c not in big:
      return False
  return True

def decode_wires(numbers):
  eight = ''.join(sorted(list(numbers.pop())))
  one = ''.join(sorted(list(numbers.pop(0))))
  seven = ''.join(sorted(list(numbers.pop(0))))
  four = ''.join(sorted(list(numbers.pop(0))))
  for _ in range(3):
    n = ''.join(sorted(list(numbers.pop())))
    if compare(n, four):
      nine = n
    elif compare(n, seven):
      zero = n
    else:
      six = n
  lower = one[0] if one[0] in six else one[1]
  for _ in range(3):
    n = ''.join(sorted(list(numbers.pop())))
    if compare(n, seven):
      three = n
    elif lower in n:
      five = n
    else:
      two = n
  return {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9
  }


filename = 'inputs/08-test.txt'
filename = 'inputs/08.txt'
with open(filename, 'r') as f:
  stuff = f.readlines()

print(part1(stuff))
print(part2(stuff))
