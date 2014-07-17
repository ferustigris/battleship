
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



class ComputerField(PlayerField):
    def __init__(self, cells, units):
        super(ComputerField, self).__init__(cells, units)
    def setUnit(self, index):
        self.cells[index].setUnit(self.freeUnits.pop())


