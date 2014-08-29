import random
from abc import abstractmethod
from mplayer import mplayer 

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
    def onBombed(self, cell):
        pass
    
    @abstractmethod
    def isReadyToPlay(self):
        pass

    @abstractmethod
    def setUnitManual(self, cell):
        pass 

class Player(AbstractPlayer):
    def __init__(self, units, game, cells):
        self.cells = cells 
        self.units = units 
        self.game = game
        self.ships = []

    def update(self, alien):
        pass 

    def arrange(self):
        self.game.onUnitsCountChange(self.units)

    def pushOn(self, game, cell):
        pass

    def onCellStateChanged(self, cell, state):
        if state == "X":
            unit = cell.decorators["unit_type"]
            if unit == 'default_unit':
                self.ships.remove(cell)
            self.units += [unit]
            self.game.onBombed(self, cell)
            self.onBombed(cell)
            mplayer.destroyUnit(unit)

    def onBombed(self, cell):
        self.game.onUnitsCountChange(self.units)

    def isReadyToPlay(self):
        return not self.units

    def setUnit(self, cell):
        unit = self.units.pop()
        cell.setUnit(unit)
        mplayer.setUnit(unit)
        if unit == 'default_unit':
            self.ships.append(cell)

    def setUnitManual(self, cell):
        self.setUnit(cell)
        self.game.onUnitsCountChange(self.units)

class AI(Player):
    def __init__(self, *args):
        Player.__init__(self, *args)
        self.lastSteps = []
        
    def update(self, alien):
        allPossibleSteps = range(len(alien.cells))
        steps = list(set(allPossibleSteps).difference(self.lastSteps))
        x = random.choice(steps)
        self.lastSteps.append(x)
        alien.cells[x].pushOn()

    def arrange(self):
        for cell in self.cells:
            cell.hide()

        indexes = range(len(self.cells))
        while self.units:
            rInd = random.choice(indexes)
            indexes.remove(rInd)
            self.setUnit(self.cells[rInd])

    def pushOn(self, game, cell):
        cell.pushOn()
        game.update()

    def setUnitManual(self, cell):
        pass 

    def onBombed(self, cell):
        self.game.onScore(1)

