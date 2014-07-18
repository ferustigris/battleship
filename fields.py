
class PlayerField(object):
    def __init__(self, cells, units):
        self.cells = cells
        self.bombed = 0
        for cell in cells:
            cell.stateObservers.append(self)
        self.freeUnits = units 

    def onCellStateChanged(self, state):
        if state == "X":
            self.bombed += 1

    def pushOn(self, game, cell):
        if cell in self.cells:
            cell.pushOn()
            game.update()

    def setUnit(self, cell):
        if cell in self.cells:
            cell.setUnit(self.freeUnits.pop())
            return len(self.freeUnits) > 0
        return False


