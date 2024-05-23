# Write your solution here:
# So, the method tick adds one second to the stopwatch. The maximum value for both seconds and minutes is 59. Your class definition should also contain a __str__ method, which returns a string representation of the state of the stopwatch, as shown in the example above.


class Stopwatch:
    def __init__(self):
        self.seconds = 58
        self.minutes = 58

    def tick(self):
        self.seconds+=1
        if self.seconds==60:
            self.seconds=0
            self.minutes+=1
            if self.minutes==60:
                self.minutes=0
    def __str__(self):
        m = f"0{self.minutes}" if 0<=self.minutes<=9 else self.minutes
        s = f"0{self.seconds}" if 0<=self.seconds<=9 else self.seconds
        return f"{m}:{s}"


watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()

        