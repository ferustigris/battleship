import random
from abc import abstractmethod

class AbstractPlayer:
    @abstractmethod
    def update(self, alienField):
        pass 

    @abstractmethod
    def arrange(self):
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

    @abstractmethod
    def setUnitManual(self, cell):
        pass 

class Player(AbstractPlayer):
    def __init__(self, units, game):
        self.field = {}# will be asigned by Field
        self.units = units 
        self.bombed = 0 
        self.game = game

    def update(self, alienField):
        pass 

    def arrange(self):
        pass 

    def pushOn(self, game, cell):
        pass

    def onCellStateChanged(self, state):
        if state == "X":
            self.bombed += 1

    def isReadyToPlay(self):
        return not self.units

    def setUnit(self, cell):
        cell.setUnit(self.units.pop())
        self.game.onUnitsCountChange(self.units)

    def setUnitManual(self, cell):
        self.setUnit(cell)

class AI(Player):
    def __init__(self, *args):
        Player.__init__(self, *args)
        self.lastSteps = []
        
    def update(self, alienField):
        allPossibleSteps = range(len(alienField.cells))
        steps = list(set(allPossibleSteps).difference(self.lastSteps))
        x = random.choice(steps)
        self.lastSteps.append(x)
        alienField.cells[x].pushOn()

    def arrange(self):
        for cell in self.field.cells:
            cell.hide()

        indexes = range(len(self.field.cells))
        while self.units:
            rInd = random.choice(indexes)
            indexes.remove(rInd)
            self.setUnit(self.field.cells[rInd])

    def pushOn(self, game, cell):
        cell.pushOn()
        game.update()

    def setUnitManual(self, cell):
        pass 


