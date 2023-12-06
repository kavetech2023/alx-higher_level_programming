#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
  """Adds two tuples.

 Defined  Args:
    tuple_a: A tuple of integers.
    tuple_b: A tuple of integers.

The Code Returns:
    A tuple with two integers:
    The first element should be the addition of the first element of each argument
    The second element should be the addition of the second element of each argument
  """

  # If either tuple is smaller than 2, use the value 0 for each missing integer.
  if len(tuple_a) < 2:
    tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
  if len(tuple_b) < 2:
    tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

  # If either tuple is bigger than 2, use only the first 2 integers.
  if len(tuple_a) > 2:
    tuple_a = tuple_a[:2]
  if len(tuple_b) > 2:
    tuple_b = tuple_b[:2]
  # Add the corresponding elements of each tuple.
  return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
