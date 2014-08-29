from levels import AbstractLevel, LevelsFactory, check
import bomblevel

def allBombed(self, player):
    """ Check, is all players units are bombed """
    return player.units.count('default_unit') == self.fieldSize()

class Level(AbstractLevel):
    def fieldSize(self):
        return 5

    def units(self):
        return ["default_unit" for i in range(self.fieldSize())]

    @check(allBombed)
    def isGameOver(self, player):
        return False

    def nextLevel(self):
        return "bomblevel"

LevelsFactory.levels["default"] = Level()

