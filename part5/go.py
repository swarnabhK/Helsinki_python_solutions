# Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. The array consists of integer values, which represent the following situations:

# 0: empty square
# 1: player 1 game piece
# 2: player 2 game piece
# The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board. Also, the size of the game board is not limited.

# The function should return the value 1 if player 1 won, and the value 2 if player 2 won. If both players have the same number of pieces on the board, the function should return the value 0.


def who_won(m):
  p1,p2 = 0,0
  for r in range(len(m)):
    for c in range(len(m[0])):
      if m[r][c]==1:
        p1+=1
      elif m[r][c]==2:
        p2+=1
  return 1 if p1>p2 else (2 if p2>p1 else 0)