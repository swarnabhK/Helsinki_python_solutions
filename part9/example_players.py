class Player:
    def __init__(self, name: str, goals: int):
        self.name = name
        self.goals = goals

    def __str__(self):
        return f"{self.name} ({self.goals} goals)"

class Team:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def add_player(self, player: "Player"):
        self.players.append(player)
    

    def summary(self):
        goals = []
        for player in self.players:
            goals.append({player.name: player.goals})
        print("Team Name: ", self.name)
        print("No of players: ", len(self.players))
        print("Goals scored by each player:", goals)


ca = Team("Campus Allstars")
ca.add_player(Player("Eric", 10))
ca.add_player(Player("Emily", 22))
ca.add_player(Player("Andy", 1))
ca.summary()
