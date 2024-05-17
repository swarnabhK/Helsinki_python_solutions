
def functionality():
  dic = {}
  while(True):
    choice = int(input("command (1 search,2 add, 3 quit): "))
    if choice==1:
      name = input("name: ")
      try:
        print(dic[name])
      except:
        pass
    elif choice==2:
      name = input("name: ")
      number = input("number: ")
      dic[name] = number
      print("ok!")
    elif choice==3:
      print("quitting...")
      break

functionality()