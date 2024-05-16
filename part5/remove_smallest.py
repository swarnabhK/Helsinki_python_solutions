# Please write a function named remove_smallest(numbers: list), which takes a list of integers as its argument.

# The functions should find and remove the smallest item in the list. You may assume there is a single smallest item in the list.

# The function should not have a return value - it should directly modify the list it receives as a parameter.

def remove_smallest(numbers):
  s= numbers[0]
  for num in numbers:
    if num<s:
      s = num
  # this is useful to delete all occurences of the minimum value, in place!
  i = 0
  while(i<len(numbers)):
    if numbers[i]==s:
      del numbers[i]
    else:
      i+=1

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5,1]
    remove_smallest(numbers)
    print(numbers)