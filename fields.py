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
        rInd = random.randrange(len(self.cells))
        self.cells[rInd].setUnit()

