from datetime import time, timedelta
from tokenize import tokenize, NUMBER, PLUS, MINUS, NAME
from io import BytesIO
from nodes import Expression, Time

class TimeCalculator:

  def print_timedelta(self, d):
    total_seconds = int(d.total_seconds())
    hours = int(total_seconds / 3600)
    minutes = int((total_seconds - hours * 3600)/60)
    print(f'{hours}:{minutes}')

  def process(self, line):
    # current_time_unit = 'h'
    # current_time = timedelta()

    tokens = [(token_type, token_val) for token_type, token_val, _, _, _ in tokenize(BytesIO(line.encode('utf-8')).readline)]
    tokens = [(token_type, token_val) for token_type, token_val in tokens if token_val != '']
    ast = Expression.try_parse(tokens[1:]) # first token is the ENCODING token
    self.print_timedelta(ast.execute())

    # for token_type, token_val, _, _, _ in tokenize(BytesIO(line.encode('utf-8')).readline):

    #   if token_type == NUMBER:
    #     if current_time_unit == 'h':
    #       current_time += timedelta(hours=int(token_val))
    #     elif current_time_unit == 'm':
    #       current_time += timedelta(minutes=int(token_val))
    #     self.print_timedelta(current_time)
    #     continue

    #   if token_val == ':':
    #     current_time_unit = 'm'
    #     continue

    #   if token_type == NAME:
    #     if token_val == 'am':
    #       pass

    #     if token_val == 'pm':
    #       current_time += timedelta(hours=12)
    #       pass

    #     if token_val == 'h':
    #       pass

    #     if token_val == 'm':
    #       pass

    #     self.print_timedelta(current_time)
    #     continue

    #   # Reset time current time
    #   current_time = timedelta()
    #   current_time_unit = 'h'

    #   if token_type == MINUS:
    #     continue

    #   if token_type == PLUS:
    #     continue
