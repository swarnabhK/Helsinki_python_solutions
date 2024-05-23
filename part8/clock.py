# Write your solution here:
# As you can see above, the constructor should take initial values for the hours, minutes and seconds as arguments, and set these appropriately. The tick method adds one second to the clock. The set method sets new values for the hours and the minutes, and sets the seconds to zero.

class Clock:
  def __init__(self,hours,minutes,seconds):
    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds
  
  def tick(self):
    self.seconds+=1
    if self.seconds==60:
      self.seconds=0
      self.minutes+=1
      if self.minutes==60:
        self.minutes=0
        self.hours+=1
        if self.hours==24:
          self.hours=0
  
  def set(self,hour,minute):
    self.hours = hour
    self.minutes = minute
    self.seconds = 0
  
  def __str__(self):
    h = f"0{self.hours}" if 0<=self.hours<=9 else self.hours
    m = f"0{self.minutes}" if 0<=self.minutes<=9 else self.minutes
    s = f"0{self.seconds}" if 0<=self.seconds<=9 else self.seconds
    return f"{h}:{m}:{s}"


clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)