def magic_string(n):
  """Returns the string "BestSchool" n times the number of the iteration."""
  my_list = []
  for i in range(n):
    my_list.append("BestSchool")
  return ''.join(my_list)
