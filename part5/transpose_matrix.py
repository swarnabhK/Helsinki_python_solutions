# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.

# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.


def transpose(matrix):
  for r in range(len(matrix)):
    for c in range(r+1,len(matrix[0])):
      matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]

m = [[1,2,3],[4,5,6],[7,8,9]]
print(m)
transpose(m)
print(m)