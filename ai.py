import random
from abc import abstractmethod

class AbstractPlayer:
    @abstractmethod
    def update(self, alienField):
        pass 

    @abstractmethod
    def arrange(self, player):
        pass 

class AI(AbstractPlayer):
    def __init__(self):
        self.lastSteps = []
        
    def update(self, alienField):
        allPossibleSteps = range(len(alienField.cells))
        steps = list(set(allPossibleSteps).difference(self.lastSteps))
        x = random.choice(steps)
        self.lastSteps.append(x)
        alienField.cells[x].pushOn()

    def arrange(self, player):
        for cell in player.cells:
            cell.hide()

        indexes = range(len(player.cells))
        while player.freeUnits:
            rInd = random.choice(indexes)
            indexes.remove(rInd)
            player.setUnit(player.cells[rInd])


class Player:
    def update(self, alienField):
        pass 

    def arrange(self, player):
        pass 


