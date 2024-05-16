# Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column indexes of a single square, as its arguments. Rows and columns are indexed from 0.

# The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly. That is, whether the block contains each of the numbers 1 to 9 at most once.



# Write your solution here

from collections import defaultdict

def block_correct(s,r,c):
  dic = defaultdict(int)
  for i in range(r,r+3):
    for j in range(c,c+3):
      if s[i][j]!=0:
        dic[s[i][j]]+=1
  for key in dic:
    if dic[key]>1:
      return False
  return True