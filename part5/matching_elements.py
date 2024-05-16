# Please write a function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers and a single integer value as its arguments. The function then counts how many elements within the matrix match the argument value.


def count_matching_elements(m,element):
  matches = 0
  for r in range(len(m)):
    for c in range(len(m[0])):
      if m[r][c]==element:
        matches+=1
  return matches


m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 1))
