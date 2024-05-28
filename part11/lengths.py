# WRITE YOUR SOLUTION HERE:
# Please write a function named lengths(lists: list) which takes a list containing lists of integers as its argument. The function should return a new list, containing the lengths of the lists within the argument list.

def lengths(lists):
  return [len(l) for l in lists]

lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
print(lengths(lists))