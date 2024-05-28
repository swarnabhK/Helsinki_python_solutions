# WRITE YOUR SOLUTION HERE:

class LotteryNumbers:
  def __init__(self,week_no,lottery_numbers):
    self.week_no = week_no
    self.lottery_numbers = lottery_numbers
  def number_of_hits(self,numbers):
    return sum([1 if num in self.lottery_numbers else 0 for num in numbers])

  def hits_in_place(self,numbers):
    return [num if num in self.lottery_numbers else -1 for num in numbers]


week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
my_numbers = [1,4,7,10,11,20,30]

print(week8.hits_in_place(my_numbers))



