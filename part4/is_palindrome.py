# Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.

# Please also write a main function which asks the user to type in words until they type in a palindrome:

# O(N), reverse the string and compare with the original string
def is_palindrome(st):
  return st==st[::-1]

#better approach, two pointers
def is_palindrome2(st):
  left,right = 0,len(st)-1
  while(left<right):
    if st[left]!=st[right]:
      return False
    left+=1
    right-=1
  return True

while(True):
  st = input("Please type in a palindrome: ")
  if is_palindrome2(st):
    print(f"{st} is a palindrome!")
    break
  else:
    print("that wasn't a palindrome.")