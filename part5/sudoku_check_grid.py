#check all 9 rows, columns and all 3x3 grids
from collections import defaultdict
def check(r):
  dic = defaultdict(int)
  for c in r:
    if c!=0:
      dic[c]+=1
  for key in dic:
    if dic[key]>1:
      return False
  return True

def check_grid(s):
  dic = defaultdict(int)
  for i in range(len(s)):
    for j in range(len(s[0])):
      if s[i][j]!=0:
        dic[s[i][j]]+=1
  for key in dic:
    if dic[key]>1:
      return False
  return True

def create_grid(s,r,c):
  grid,row = [],[]
  for i in range(r,r+3):
    row = []
    for j in range(c,c+3):
      row.append(s[i][j])
    grid.append(row)
  return grid

def sudoku_grid_correct(sudoku):
  # check rows, send each row every time
  for row in sudoku:
    if not check(row):
      return False
  #check columns, send each column every time
  cols = []
  for col in range(len(sudoku[0])):
    cols = []
    for row in sudoku:
      cols.append(row[col])
    if not check(cols):
      return False
    
  #check all 3x3 grids, send each grid everytime
  idxs = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
  for r,c in idxs:
    grid = create_grid(sudoku,r,c)
    if not check_grid(grid):
      return False
  return True
  

  

sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))
sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]
print(sudoku_grid_correct(sudoku2))
