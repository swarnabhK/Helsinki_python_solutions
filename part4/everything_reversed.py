# Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.

def reverse(w):
  left,right = 0, len(w)-1
  w = list(w)
  while(left<right):
    w[left],w[right] = w[right],w[left]
    left+=1
    right-=1
  return "".join(w)

def everything_reversed(l):
  res = []
  for word in l:
    res.append(reverse(word))
  return res[::-1]


my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)
