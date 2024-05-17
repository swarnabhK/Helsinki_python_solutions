# Please write an improved version of the phone book application. Each entry should now accommodate multiple phone numbers. The application should work otherwise exactly as above, but this time all numbers attached to a name should be printed.

dic = {}
while(True):
  choice = int(input("command (1 search, 2 add, 3 quit): "))
  if choice==2:
    name = input("name: ")
    number = input("number: ")
    if name not in dic:
      dic[name] = []
    dic[name].append(number)
    print("ok!")
  elif choice==1:
    name = input("name: ")
    try:
      for no in dic[name]:
        print(no)
    except:
      print("no number")
  elif choice==3:
    print("quitting...")
    break

