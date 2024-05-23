# Write your solution here

def read_input(inp,lo,hi):
  while True:
    try:
      no = int(input(inp))
      if lo<=no<=hi:
        return no
    except:
      pass
    print(f"You must type in an integer between {lo} and {hi}")


number = read_input("Enter a number: ",5, 10)
print("You typed in:", number)