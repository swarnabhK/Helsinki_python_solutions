# Please write a function named histogram, which takes a string as its argument. The function should print out a histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented by a star on the specific line for that letter.

# For example, the function call histogram("abba") should print out


from collections import defaultdict
def histogram(s):
  dic = defaultdict(int)
  for c in s:
    dic[c]+=1
  for key,value in dic.items():
    print(f"{key}: {value*"*"}")


histogram("statistically")