# Please write three functions: first_word, second_word and last_word. Each function takes a string argument.

# As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.

# In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character. There will be no spaces in the beginning or at the end of the argument strings.

def first_word(st):
  st = st.split(" ")
  return st[0]

def second_word(st):
  st = st.split(" ")
  return st[1]

def last_word(st):
  st = st.split(" ")
  return st[-1]



# sentence = "it was a dark and stormy python"
# print(first_word(sentence)) # it
# print(second_word(sentence)) # was
# print(last_word(sentence)) # python


#approach 2: without using split
def first_word2(st):
  s = ""
  for c in st:
    if c==" ":
      break
    else:
      s+=c
  return s

def second_word2(st):
  s,spaces = "",0
  for c in st:
    if c==" ":
      spaces+=1
      if spaces==1:
        s=""
      if spaces==2:
        break
    else:
      s+=c
  return s

def last_word2(st):
  s = ""
  for i in range(len(st)-1,-1,-1):
    if st[i]==" ":
      break
    else:
      s+=st[i]
  return s[::-1]

sentence = "it was a dark and stormy python"
print(first_word2(sentence)) # it
print(second_word2(sentence)) # was
print(last_word2(sentence)) # was

