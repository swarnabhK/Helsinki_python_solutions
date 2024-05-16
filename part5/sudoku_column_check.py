# Please write a function named column_correct(sudoku: list, column_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single column, as its arguments. Columns are indexed from 0.

# The function should return True or False, depending on whether the column is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.


# Write your solution here
from collections import defaultdict
def column_correct(s,col):
  dic = defaultdict(int)
  for r in s:
    if r[col]!=0:
      dic[r[col]]+=1
  for key in dic:
    if dic[key]>1:
      return False
  return True