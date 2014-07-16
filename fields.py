import units

class PlayerField(object):
    def __init__(self, cells):
        self.cells = cells
        self.freeUnits = [units.UnitCellState() for i in range(3)]

class ComputerField(PlayerField):
    def __init__(self, cells):
        super(ComputerField, self).__init__(cells)
    def setUnit(self, index):
        self.cells[index].setUnit(self.freeUnits.pop())


