# Please write a function named remove_smaller_than(numbers: list, limit: int) which takes a list of integers and a limit value (also in integer format) as its arguments.

# The function should use a list comprehension to produce a new list without the values which are smaller than the limit value.



def remove_smaller_than(numbers,limit):
  return [num for num in numbers if num>=limit]


numbers = [1,65, 32, -6, 9, 11]
print(remove_smaller_than(numbers, 10))

print(remove_smaller_than([-4, 7, 8, -100], 0))
