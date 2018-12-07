from datetime import time, timedelta
from .Node import Node
from tokenize import NUMBER

class Time(Node):

  def __init__(self, t):
    self.t = t


  def execute(self):
    return self.t


  @classmethod
  def try_parse(cls, tokens):
    hours = 0
    minutes = 0

    type = None
    
    token, tokens = cls.consume_type(NUMBER, tokens)
    if token is None:
      return None
    _, token_val = token
    num = int(token_val)    

    (_, token_val), tokens = cls.consume_val([':', 'h', 'm', 'am', 'pm'], tokens)
    if token_val == ':':
      hours = num
      type = 'time'
    elif token_val == 'h':
      hours = num
      type = 'duration'
      if not cls.peek_type(NUMBER, tokens):
        return Time(timedelta(hours=hours, minutes=minutes)), tokens
    elif token_val == 'm':
      minutes = num
      type = 'duration'
      return Time(timedelta(hours=hours, minutes=minutes)), tokens
    elif token_val == 'am':
      hours = num
      type = 'time'
      return Time(timedelta(hours=hours)), tokens
    elif token_val == 'pm':
      hours = num + 12 if num < 12 else num
      type = 'time'
      return Time(timedelta(hours=hours)), tokens

    token, tokens = cls.consume_type(NUMBER, tokens)
    _, token_val = token
    num = int(token_val)
    minutes = num

    if type == 'time':
      (_, token_val), tokens = cls.consume_val(['am', 'pm'], tokens)
      if token_val == 'am':
        return Time(timedelta(hours=hours, minutes=minutes)), tokens
      elif token_val == 'pm':
        if hours < 12:
          hours += 12
        return Time(timedelta(hours=hours, minutes=minutes)), tokens
    elif type == 'duration':
      _, tokens = cls.consume_val(['m'], tokens)
      minutes = num
      return Time(timedelta(hours=hours, minutes=minutes)), tokens
