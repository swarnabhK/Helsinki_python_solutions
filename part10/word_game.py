# Write your solution here
# we inherited the word game class in three other classes. We overriden the method round_winner for all three classes based on the specific game
# functionality(rule)

import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self,rounds):
        super().__init__(rounds)
    
    def round_winner(self,player1_word,player2_word):
        if len(player1_word)>len(player2_word):
            return 1
        elif len(player2_word)>len(player1_word):
            return 2
        else:
            return 0

class MostVowels(WordGame):
    def __init__(self,rounds):
        super().__init__(rounds)
    
    def round_winner(self,player1_word,player2_word):
        vowels = "aeiou"
        p1_v = sum(c in vowels for c in player1_word)
        p2_v = sum(c in vowels for c in player2_word)
        
        if p1_v>p2_v:
            return 1
        elif p2_v>p1_v:
            return 2
        else:
            return 0
        
class RockPaperScissors(WordGame):
    def __init__(self,rounds):
        super().__init__(rounds)
    
    def round_winner(self,p1,p2):
        valid_choices = ("paper","rock","scissors")
        if p1 in valid_choices and p2 not in valid_choices:
            return 1
        elif p2 in valid_choices and p1 not in valid_choices:
            return 2
        elif p1 not in valid_choices and p2 not in valid_choices:
            return 0
        else:
            defeats = {'rock':'scissors','paper':'rock','scissors':'paper'}
            if defeats[p1]==p2:
                return 1
            elif defeats[p2]==p1:
                return 2
            elif p1==p2:
                return 0


p = RockPaperScissors(4)
p.play()
