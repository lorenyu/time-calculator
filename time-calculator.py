#!/usr/bin/env python
import sys
from TimeCalculator import TimeCalculator

print('Type "quit" to exit')
calculator = TimeCalculator()
while True:
  line = sys.stdin.readline().strip()
  if line == 'quit':
    break
  try:
    calculator.process(line)
  except Exception as error:
    print(f'Error: {error}', file=sys.stderr)
