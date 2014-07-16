import random

class PlayerField:
    def __init__(self, cells):
        self.cells = cells
    def arrange(self):
        pass

class ComputerField:
    def __init__(self, cells):
        self.cells = cells
    def arrange(self):

        for cell in self.cells:
            cell.hide()

        rInd = random.randrange(len(self.cells))
        self.cells[rInd].setUnit()
        rInd = random.randrange(len(self.cells))
        self.cells[rInd].setUnit()

