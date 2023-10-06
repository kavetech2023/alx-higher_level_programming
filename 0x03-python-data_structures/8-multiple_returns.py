#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
  """Returns a tuple with the length of a string and its first character.

  Args:
    sentence:It is a string.

  Returns:
    A tuple with two elements:
    The first element is the length of the string.
    The second element is the first character of the string, or None if the string is empty.
  """

  if sentence == "":
    return (0, None)
  else:
    return (len(sentence), sentence[0])
