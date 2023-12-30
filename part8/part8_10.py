class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.initial_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if(self.value>0):
          self.value-=1

    # define the rest of your methods here
    def set_to_zero(self):
        self.value=0
    
    def reset_original_value(self):
        self.value = self.initial_value



#Part 1
counter = DecreasingCounter(10)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()

#Part2
counter = DecreasingCounter(2)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()

#Part 3

counter = DecreasingCounter(100)
counter.print_value()
counter.set_to_zero()
counter.print_value()

#Part 4

counter = DecreasingCounter(55)
counter.decrease()
counter.decrease()
counter.decrease()
counter.decrease()
counter.print_value()
counter.reset_original_value()
counter.print_value()
