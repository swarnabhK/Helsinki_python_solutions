# Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments. Rows are indexed from 0.

# The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.


from collections import defaultdict
def row_correct(s,row):
  r = s[row]
  dic = defaultdict(int)
  for n in r:
    if n!=0:
      dic[n]+=1
  for key in dic:
    if dic[key]>1:
      return False
  return True