# Write your solution here
import re
def find_words(search_term):
  matches = []
  with open("words.txt", 'r') as f:
    if '.' in search_term:
      pattern = search_term.replace('.', r"\w")
      for line in f:
        word = line.strip()
        if re.match(pattern, word) and len(word)==len(search_term):
          matches.append(word)
    elif "*" in search_term:
      if search_term[0]=='*':
        for line in f:
          word = line.strip()
          if word.endswith(search_term[1:]):
            matches.append(word)
      elif search_term[-1]=='*':
        for line in f:
          word = line.strip()
          if word.startswith(search_term[:-1]):
            matches.append(word)
    else:
      for line in f:
        word = line.strip()
        if search_term==word:
          matches.append(word)
  return matches
