# WRITE YOUR SOLUTION HERE:
# Please write a function named rows_of_stars(numbers: list) which takes a list of integers as its argument. The function should return a new list containing rows of stars. The length of each row should correspond to the integer at the same index in the original list. The function should use a list comprehension to achieve this.

def rows_of_stars(numbers):
  return ['*'*num for num in numbers]


rows = rows_of_stars([1,2,3,4])
for row in rows:
    print(row)

print()

rows = rows_of_stars([4, 3, 2, 1, 10])
for row in rows:
    print(row)
