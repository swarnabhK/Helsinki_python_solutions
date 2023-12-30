#Emulate a clock functionality
class Clock:
    def __init__(self,hours,minutes,seconds) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def tick(self):
        self.seconds+=1
        if(self.seconds==60):
            self.seconds = 0
            self.minutes+=1
            if(self.minutes==60):
                self.minutes = 0
                self.hours+=1
                if(self.hours==24):
                    self.hours = 0
    
    def set(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0
        
    def __str__(self):
        minute = f"0{self.minutes}" if 0<=self.minutes<=9 else f"{self.minutes}"
        second = f"0{self.seconds}" if 0<=self.seconds<=9 else f"{self.seconds}"
        hour = f"0{self.hours}" if 0<=self.hours<=9 else f"{self.hours}"
        return f"{hour}:{minute}:{second}"


#Tests
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
