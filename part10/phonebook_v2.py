
# Write your solution here:
class Person:
    def __init__(self,name):
        self.__name = name
        self.__numbers = []
        self.__address = None
    
    def add_number(self,number):
        self.__numbers.append(number)
    
    def add_address(self,address):
        self.__address = address
    
    def numbers(self):
        return self.__numbers
    
    def address(self):
        return self.__address
    
    def name(self):
        return self.__name
    

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

    def add_number(self,name,number):
        if name in self.__persons:
            p = self.__persons[name]
            p.add_number(number)
            self.__persons[name] = p
        else:
            person = Person(name)
            person.add_number(number) 
            self.__persons[name] = person

    def add_address(self,name,address):
        if name in self.__persons:
            p = self.__persons[name]
            p.add_address(address)
            self.__persons[name] = p
        else:
            person = Person(name)
            person.add_address(address)
            self.__persons[name] = person
        
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name,number)
        

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name,address)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)

        try:
            numbers = person.numbers()
            if numbers == []:
                print("number unknown")  
            for number in numbers:
                print(number)
            address = person.address()
            if address is not None:
                print(address)
            else:
                print("address unkown")
        except:
            print("address unkown")
            print("number unkown")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command =="3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

