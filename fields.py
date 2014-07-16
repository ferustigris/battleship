import random
import units

class PlayerField(object):
    def __init__(self, cells):
        self.cells = cells
        self.freeUnits = [units.UnitCellState() for i in range(3)]

    def arrange(self):
        pass

class ComputerField(PlayerField):
    def __init__(self, cells):
        super(ComputerField, self).__init__(cells)

    def arrange(self):

        for cell in self.cells:
            cell.hide()

        while self.freeUnits:
            rInd = random.randrange(len(self.cells))
            self.cells[rInd].setUnit(self.freeUnits.pop())

