
class Game:
    def __init__(self):
        self.wins=0
        self.loss=0

    def won_level(self):
        self.wins+=1

    def lost_level(self):
        self.loss+=1

    @property
    def score(self):
        return self.wins-self.loss

s=Game()
s.won_level()
s.won_level()
s.lost_level()
print(s.score)