from random import choice
def words(n,bg):
  w,res,res_s = [],[],set()
  with open("words.txt","r") as file:
    for line in file:
      word = line.strip()
      if word.startswith(bg):
        w.append(word)
  if len(w)<n:
    raise ValueError()
  while len(res)<n:
    wd = choice(w)
    if wd in res_s:
      continue
    res_s.add(wd)
    res.append(wd)
  return res

print(words(5,"ca"))