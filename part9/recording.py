# WRITE YOUR SOLUTION HERE:
# Please create a class named Recording which models a single recording. The class should have one private variable: __length of type integer.
# Please implement the following:
# a constructor which takes the length as an argument
# a getter method length which returns the length of the recording
# a setter method which sets the length of the recording


class Recording:
  def __init__(self,length):
    self.__length = length

  # the attribute for which we are defining a getter and setter method and the getter and setter methods have the same name. In this case
  # property decorator defines that this property is offered to the client.
  @property
  def length(self):
    return self.__length

  # we use the property.setter to make sure this is a setter method.
  # length. It's always a good idea to raise an exception to let the client know that the supplied value to a setter method is not acceptable.
  @length.setter
  def length(self,length):
    self.__length = length
  

the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)

