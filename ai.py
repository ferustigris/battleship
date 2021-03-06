import random
from abc import abstractmethod
from mplayer import mplayer 
from kivy.clock import Clock 

class AbstractPlayer:
    @abstractmethod
    def update(self, enemyCells):
        pass 

    @abstractmethod
    def arrange(self, cells, field):
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
    def setUnitManual(self, _, cell):
        pass 

def CheckLastSteps(func):
    '''Check has step been made'''
    steps = []

    def __CheckLastSteps(self, game, cell):
        if cell in steps:
            return False
        steps.append(cell)
        return func(self, game, cell)
    return __CheckLastSteps
    
class Player(AbstractPlayer):
    def __init__(self, units, game):
        self.units = units 
        self.game = game
        self.ships = []

    def update(self, enemy):
        pass 

    def arrange(self, cells, field):
        self.game.onUnitsCountChange(self.units)
        field.activate()

    @CheckLastSteps
    def pushOn(self, game, cell):
        return False

    def onCellStateChanged(self, cell, state):
        if state == "X":
            unit = cell.decorators["unit_type"]
            if unit == 'default_unit':
                self.ships.remove(cell)
            self.units += [unit]
            self.game.onBombed(self, cell)
            self.onBombed(cell)
            mplayer.destroyUnit(unit)
        else:
            mplayer.destroyUnit('empty')

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

    @CheckLastSteps
    def setUnitManual(self, _, cell):
        self.setUnit(cell)
        self.game.onUnitsCountChange(self.units)

    def getNealestKoords(self, x, y):
        return map(lambda i, j: (x + i, y + j), [0, 0, -1, 1], [-1, 1, 0, 0])

class AI(Player):
    def __init__(self, *args):
        Player.__init__(self, *args)
        self.lastSteps = []
        
    def update(self, enemyCells):
        allPossibleSteps = range(len(enemyCells))
        steps = list(set(allPossibleSteps).difference(self.lastSteps))
        x = random.choice(steps)
        self.lastSteps.append(x)
        enemyCells[x].pushOn()
        return True

    def arrange(self, cells, field):
        for cell in cells:
            cell.hide()

        indexes = range(len(cells))
        while self.units:
            rInd = random.choice(indexes)
            indexes.remove(rInd)
            koords = self.getNealestKoords(cells[rInd].x, cells[rInd].y)
            indexesToRemove = [i for i in indexes if (cells[i].x, cells[i].y) in koords]
            indexes = [x for x in set(indexes).difference(indexesToRemove)]
            self.setUnit(cells[rInd])
        field.deactivate()

    @CheckLastSteps
    def pushOn(self, game, cell):
        cell.pushOn()
        Clock.schedule_once(lambda x: game.update(), 1)
        return True

    def setUnitManual(self, _, cell):
        pass 

    def onBombed(self, cell):
        self.game.onScore(1)

