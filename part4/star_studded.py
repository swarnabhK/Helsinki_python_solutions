# Please write a program which asks the user to type in a string. The program then prints each input character on a separate line. After each character there should be a star (*) printed on its own line.

st = input("Please type in a string: ")
for c in st:
  print(c)
  print("*"+"\n")