class EmptyCellState:
    def representation(self):
        return "."
    def transfer(self):
        pass

class Cell:
    def __init__(self):
        self.state = "."

    def setUnit(self):
        self.state = "0"
    
    def check(self):
        self.state = "X"
