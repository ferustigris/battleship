from levels import AbstractLevel, LevelsFactory, check

from cell import Cell
import cellstates 

def allBombed(self, player):
    """ Check, is all players units are bombed """
    return  player.bombed == self.fieldSize()

class Level(AbstractLevel):
    def fieldSize(self):
        return 5

    def units(self):
        return ["default_unit" for i in range(self.fieldSize())]

    def cells(self):
        return [Cell() for i in range(self.fieldSize() ** 2)]

    @check(allBombed)
    def isGameOver(self, player):
        return False

    def nextLevel(self):
        import bomblevel
        return "bomblevel"

LevelsFactory.levels["default"] = Level()
