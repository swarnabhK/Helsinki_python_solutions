# Please write a function named length which takes a list as its argument and returns the length of the list.


def length(l: list)->int:
  return len(l)


my_list = [1, 2, 3, 4, 5]
result = length(my_list)
print("The length is", result)

# the list given as an argument doesn't need to be stored in any variable
result = length([1, 1, 1, 1])
print("The length is", result)
