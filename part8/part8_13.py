class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    def tick(self):
        if(self.seconds==59):
            self.minutes+=1
            self.seconds = 0
            if(self.minutes==60):
              self.minutes = 0
        else:
            self.seconds+=1
    def __str__(self):
        if(self.minutes>=0 and self.minutes<=9):
            minute=f"0{self.minutes}"
        else:
            minute = f"{self.minutes}"
        if(self.seconds>=0 and self.seconds<=9):
            second = f"0{self.seconds}"
        else:
            second = f"{self.seconds}"
        return f"{minute}:{second}"
  

watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()
