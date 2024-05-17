# write your solution here
# The file matrix.txt contains a matrix in the format specified in the example below:
# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc...
# Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.
# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. For example, calling row_sums when the matrix in the file is defined as


def matrix_sum():
  s = 0
  with open("matrix.txt") as new_file:
    for line in new_file:
      line = line.replace("\n","")
      line = line.split(",")
      line = list(map(int, line))
      s+=sum(line)
  return s

def matrix_max():
  mo = -float("inf")
  with open("matrix.txt") as new_file:
    for line in new_file:
      line = line.replace("\n","")
      line = line.split(",")
      line = list(map(int, line))
      m = max(line)
      mo = max(m,mo)
  return mo

def row_sums():
  l = []
  with open("matrix.txt") as new_file:
    for line in new_file:
      line = line.replace("\n","")
      line = line.split(",")
      line = list(map(int, line))
      l.append(sum(line))
  return l

print(matrix_sum())
print(matrix_max())
print(row_sums())