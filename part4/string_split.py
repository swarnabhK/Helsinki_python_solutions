# split strings without using the builtin split function. The character to split on can be any character.


def split(st,char):
  words,word = [],""
  for w in st:
    if w==char:
      words.append(word)
      word = ""
    else:
      word+=w
  words.append(word)
  return words

print(split("My#name#is#Swarnabh#Kashyap","#"))
print(split("Arsenal are winning the league  "," "))
print(split("Arsenal are winning the league  innit bruv","t"))