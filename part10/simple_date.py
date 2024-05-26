# WRITE YOUR SOLUTION HERE:

class SimpleDate:
  def __init__(self,dd,mm,yyyy):
    self.dd = dd
    self.mm = mm
    self.yyyy = yyyy
  
  def __gt__(self,another):
    if self.yyyy>another.yyyy:
      return True
    elif self.yyyy==another.yyyy:
      if self.mm>another.mm:
        return True
      elif self.mm==another.mm:
        if self.dd>another.dd:
          return True
    return False

  def __lt__(self,another):
    if self.yyyy<another.yyyy:
      return True
    elif self.yyyy==another.yyyy:
      if self.mm<another.mm:
        return True
      elif self.mm==another.mm:
        if self.dd<another.dd:
          return True
    return False
  
  def __eq__(self,another):
    return self.yyyy==another.yyyy and self.mm==another.mm and self.dd==another.dd
  
  def __ne__(self,another):
    return not self.__eq__(another)

  def __str__(self):
    return f"{self.dd}.{self.mm}.{self.yyyy}"
  
  def __add__(self,days):
    mm,yy = 0,0
    y,rem = days//360,days%360
    m,d = rem//30,rem%30
    if d+self.dd>30:
      mm+=1
    if m+self.mm>12:
      yy+=1
    dd = (d+self.dd)%30
    mm=(mm+m+self.mm)%12
    yy+=y+self.yyyy
    return SimpleDate(dd,mm,yy)

  def __sub__(self,another):
    y = self.yyyy - another.yyyy
    m = self.mm - another.mm
    d = self.dd - another.dd
    s = y*360+m*30+d
    return abs(s)


d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(2, 11, 2020)
d3 = SimpleDate(28, 12, 1985)

print(d2-d1)
print(d1-d2)
print(d1-d3)


