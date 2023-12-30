"""Please write a function named row_sums(my_matrix: list), which takes an integer matrix as its argument.

The function should add a new element on each row in the matrix. This element contains the sum of the other elements on that row. The function does not have a return value. It should modify the parameter matrix in place.

"""


def row_sums(my_matrix):
    for row in my_matrix:
      row.append(sum(num for num in row))


my_matrix = [[1, 2], [3, 4]]
print("Before changes:",my_matrix)
row_sums(my_matrix)
print("After changes:",my_matrix)