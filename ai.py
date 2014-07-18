import random
from abc import abstractmethod

class AbstractPlayer:
    @abstractmethod
    def update(self, alienField):
        pass 

    @abstractmethod
    def arrange(self, player):
        pass 
    
    @abstractmethod
    def pushOn(self, game, cell):
        pass
    
    @abstractmethod
    def onCellStateChanged(self, state):
        pass
    
    @abstractmethod
    def isReadyToPlay(self):
        pass


class Player(AbstractPlayer):
    def __init__(self):
        self.field = {}# will be asigned by Field
        self.bombed = 0 

    def update(self, alienField):
        pass 

    def arrange(self, player):
        pass 

    def pushOn(self, game, cell):
        pass

    def onCellStateChanged(self, state):
        if state == "X":
            self.bombed += 1

    def isReadyToPlay(self):
        return len(self.field.freeUnits) == 0


class AI(Player):
    def __init__(self):
        Player.__init__(self)
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

    def pushOn(self, game, cell):
        cell.pushOn()
        game.update()

