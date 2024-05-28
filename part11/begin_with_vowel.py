# WRITE YOUR SOLUTION HERE:
# Please write a function named begin_with_vowel(words: list) which takes a list of strings as its argument

def begin_with_vowel(words):
  return [w for w in words if w[0].lower() in 'aeiou']


word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
for vowelled in begin_with_vowel(word_list):
    print(vowelled)
