# Please write a function named range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.

def range_of_list(l: list)->int:
  return max(l)-min(l)


my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list)
print("The range of the list is", result)
