#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
  """Finds the biggest integer of a list.

  Args:
    my_list: A list of integers.

  Returns:
    The big integer of the list, or None if the list is empty.
  """

  if my_list == []:
    return None
  else:
    big_integer = my_list[0]
    for integer in my_list:
      if integer > big_integer:
        big_integer = integer
    return big_integer
