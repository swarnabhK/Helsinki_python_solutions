# Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.


from collections import defaultdict


# O(NlogN) solution. 
def is_anagram(st1,st2):
  return sorted(st1)==sorted(st2)

# O(N) solution.
def compare_dicts(d1,d2):
  if len(d1)!=len(d2):
    return False
  for key,value in d1.items():
    if key not in d2 or d2[key]!=value:
      return False
  return True

def is_anagram2(st1,st2):
  dic1,dic2 = defaultdict(int),defaultdict(int)
  for c in st1:
    dic1[c]+=1
  for c in st2:
    dic2[c]+=1
  return compare_dicts(dic1,dic2)


print(is_anagram2("tame", "meta")) # True
print(is_anagram2("tame", "mate")) # True
print(is_anagram2("tame", "team")) # True
print(is_anagram2("tabby", "batty")) # False
print(is_anagram2("python", "java")) # False
