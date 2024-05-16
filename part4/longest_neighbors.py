# Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1. So, items 1 and 2 would be neighbours, and so would items 56 and 55.

# Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.

# For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.


def longest_series_of_neighbors(l):
  count,longest = 1,0
  left,right = 0,1
  while(right<len(l)):
    if(abs(l[left]-l[right])==1):
      count+=1
      longest = max(count,longest)
    else:
      count = 1
    left+=1
    right+=1
  return longest

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbors(my_list))


