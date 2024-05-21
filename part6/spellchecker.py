# Please write a program which asks the user to type in some text. 
# Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them

def create_dictionary():
  words = set()
  with open("wordlist.txt") as ws:
    for line in ws:
      line = line.strip()
      words.add(line)
  return words

def process_input():
  wd = create_dictionary()
  s = input("Write text: ")
  res = ""
  s = s.split()
  for i,w in enumerate(s):
    if w.lower() not in wd:
      s[i] = f"*{w}*"
  print(" ".join(s))

process_input()
