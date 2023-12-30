class Recording:
    def __init__(self,length) -> None:
        if(length<0):
            raise ValueError("The length cannot be negative.")
        self.__length = length

    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self,length):
        if(length<0):
          raise ValueError("The length cannot be negative.")
        self.__length = length
        
the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)