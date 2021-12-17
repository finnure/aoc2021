class Card():
  def __init__(self, lines) -> None:
    self.done = False
    self.rows = [[int(n) for n in line.split()] for line in lines[1:]]
    self.cols = [[line[i] for line in self.rows] for i in range(len(self.rows[0]))]

  def play(self, number):
    if self.done:
      return
    if self.row(number):
      self.done = True
      return True
    if self.col(number):
      self.done = True
      return True

  def row(self, number):
    for line in self.rows:
      try:
        line.pop(line.index(number))
        if len(line) == 0:
          return True
      except ValueError:
        pass
    return False
  
  def col(self, number):
    for line in self.cols:
      try:
        line.pop(line.index(number))
        if len(line) == 0:
          return True
      except ValueError:
        pass
    return False

  def sum(self, number):
    return sum([sum(line) for line in self.rows]) * number

  def __str__(self) -> str:
    return str(self.rows) + str(self.cols)


def part1(numbers, cards):
  for n in numbers:
    for card in cards:
      if card.play(n):
        return card.sum(n)

def part2(numbers, cards):
  total_cards = len(cards)
  for n in numbers:
    for card in cards:
      if card.play(n):
        if total_cards == 1:
          return card.sum(n)
        total_cards -= 1


with open('inputs/04.txt', 'r') as f:
  numbers = f.readline()
  numbers = [int(n) for n in numbers.strip().split(',')]
  rest = f.readlines()
  cards1 = [Card(rest[i:i+6]) for i in range(0, len(rest), 6)]
  cards2 = [Card(rest[i:i+6]) for i in range(0, len(rest), 6)]


print(part1(numbers, cards1))
print(part2(numbers, cards2))



