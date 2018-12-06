from .Node import Node
from .Time import Time

class Expression(Node):

  def __init__(self, operation, left, right):
    self.left = left
    self.right = right
    self.operation = operation


  def execute(self):
    left = self.left.execute()
    right = self.right.execute()
    if self.operation == '+':
      return left + right
    elif self.operation == '-':
      return left - right


  @classmethod
  def try_parse(cls, tokens):
    t, tokens = Time.try_parse(tokens)

    if cls.is_end(tokens):
      return t

    (_, token_val), tokens = cls.consume_val(['+', '-'], tokens)
    operation = token_val
    
    e = Expression.try_parse(tokens)
    return Expression(operation, t, e)
