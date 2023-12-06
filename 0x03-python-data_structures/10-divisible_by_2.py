def divisible_by_2(my_list=[]):
  """Finds all multiples of 2 in a list.

  Args:
    my_list: A list of integers.

  Returns:
    A new list with True or False.
    The new list should have the same size as the original list.
  """

  new_list = []
  for i in my_list:
    if i % 2 == 0:
      new_list.append(True)
    else:
      new_list.append(False)
  return new_list
