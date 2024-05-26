# Please create a class named ListHelper which contains the following two class methods.
# greatest_frequency(my_list: list) returns the most common item on the list
# doubles(my_list: list) returns the number of unique items which appear at least twice on the list
# It should be possible to use these methods without creating an instance of the class. An example of how the methods could be used:

from collections import defaultdict
class ListHelper:
  @classmethod
  def greatest_frequency(cls,my_list):
    dic,g,gg = defaultdict(int),float("-inf"),0
    for num in my_list:
      dic[num]+=1
    for k in dic:
      if dic[k]>g:
        g = dic[k]
        gg = k
    return gg
  @classmethod
  def doubles(cls,my_list):
    dic,c = defaultdict(int),0
    for num in my_list:
      dic[num]+=1
    for k in dic:
      if dic[k]>1:
        c+=1
    return c


numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))