# Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at each index in the two original lists. You may assume both lists have the same number of items.

def list_sum(l1,l2):
  result = [0]*len(l1)
  for i in range(len(l1)):
    result[i] = l1[i]+l2[i]
  return result


a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 10, 12]
