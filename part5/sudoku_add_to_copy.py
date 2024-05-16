# This is the very last sudoku task. This time we will create a slightly different version of the function for adding new numbers to the grid.

# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.


def print_sudoku(sudoku):
  char = ""
  for i in range(len(sudoku)):
    for j in range(len(sudoku[0])):
      if sudoku[i][j]==0:
        char = "_"
      else:
        char = sudoku[i][j]
      if (i==2 or i==5) and j==8:
        print(f"{char}",end="\n")
      elif j==2 or j==5:
        print(f"{char}",end="  ")
      else:
        print(f"{char}",end=" ")
    print()

def copy_and_add(sudoku,r,c,number):
  rows,cols = len(sudoku),len(sudoku[0])
  grid = [[0 for _ in range (cols)] for _ in range(rows)]
  for i in range(rows):
    for j in range(cols):
      if i==r and j==c:
        grid[i][j] = number
  return grid

sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

grid_copy = copy_and_add(sudoku, 0, 0, 2)
print("Original:")
print_sudoku(sudoku)
print()
print("Copy:")
print_sudoku(grid_copy)
