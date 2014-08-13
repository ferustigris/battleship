from levels import AbstractLevel

from cell import Cell
import cellstates 

class Level(AbstractLevel):
    def fieldSize(self):
        return 5

    def units(self):
        return ["default_unit" for i in range(self.fieldSize())]

    def cells(self):
        return [Cell() for i in range(self.fieldSize() ** 2)]

    def isGameOver(self, players):
        for player in players:
            if player.bombed == self.fieldSize():
                return True
        return False
 
