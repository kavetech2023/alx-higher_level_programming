#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
  """Prints the first x elements of a list, handling potential IndexError.

  Args:
    my_list: The list to print elements from.
    x: The number of elements to print (defaults to all elements).

  Returns:
    The number of elements successfully printed.
  """

  sum_total = 0
  for i in range(x):
    try:
      print(f"{my_list[i]}", end="")
      sum_total += 1
    except IndexError:
      break
  print()
  return sum_total
