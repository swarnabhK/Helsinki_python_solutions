# Write your solution here
# Please write a function named roll(die: str), which rolls the die specified by the argument. 
# Also write a function named play(die1: str, die2: str, times: int), which throws both dice as many times as specified by the third argument. The function should return a tuple. The first item should be the number of times die 1 won, the second the number of times die 2 won, and the third item should be the number of ties.

from random import choice


def roll(die):
  if die=="A":
    c = choice(die_a)
  elif die=="B":
    c = choice(die_b)
  elif die=="C":
    c = choice(die_c)
  return c

def play(die1,die2,times):
  a_wins,b_wins,ties = 0,0,0
  for i in range(times):
    a,b = roll(die1),roll(die2)
    if a>b:
      a_wins+=1
    elif b>a:
      b_wins+=1
    else:
      ties+=1
  return a_wins,b_wins,ties

die_a = [3,3,3,3,3,6]
die_b = [2,2,2,5,5,5]
die_c = [1,4,4,4,4,4]

result = play("A", "C", 1000)
print(result)
result = play("B", "B", 1000)
print(result)

