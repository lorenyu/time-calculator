import sys
from TimeCalculator import TimeCalculator

print('Type "quit" to exit')
calculator = TimeCalculator()
while True:
  line = sys.stdin.readline().strip()
  if line == 'quit':
    break
  print(f'processing line {line}')
  calculator.process(line)
