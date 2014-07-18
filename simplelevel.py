from levels import AbstractLevel

from cell import Cell
import cellstates 

class Level(AbstractLevel):
    def fieldSize(self):
        return 5
    def units(self):
        return [cellstates.UnitCellState() for i in range(self.fieldSize())]
    def cells(self):
        return [Cell() for i in range(self.fieldSize() ** 2)]

