class Node:

  @classmethod
  def is_end(cls, tokens):
    return len(tokens) == 0


  @classmethod
  def consume(cls, tokens):
    if cls.is_end(tokens):
      raise Exception('End of tokens')
    return tokens[0], tokens[1:]


  @classmethod
  def consume_type(cls, expected_token_type, tokens):
    token, rest = cls.consume(tokens)
    token_type, token_val = token

    if token_type != expected_token_type:
      raise Exception(f'Token {token_val} with token type {token_type} does not match expected token type {expected_token_type}')

    return token, rest

  @classmethod
  def consume_val(cls, expected_token_vals, tokens):
    token, rest = cls.consume(tokens)
    _, token_val = token

    if token_val not in expected_token_vals:
      expected_str = ','.join(expected_token_vals)
      raise Exception(f'Token {token_val} does not match one of expected token values {expected_str}')

    return token, rest


  @classmethod
  def peek_type(cls, expected_token_type, tokens):
    if cls.is_end(tokens):
      return False

    if tokens[0][0] != expected_token_type:
      return False

    return True
