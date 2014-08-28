from levels import AbstractLevel, LevelsFactory, check

from cell import Cell
import cellstates 

def bombBombed(self, player):
    """ Check, is bomb was bombed """
    return "nuclear_bomb_unit" in player.units

def allBombed(self, player):
    """ Check, is all players units are bombed """
    return  player.bombed == self.fieldSize()

class Level(AbstractLevel):
    def fieldSize(self):
        return 5 

    def units(self):
        return ["nuclear_bomb_unit"] + ["default_unit" for i in range(self.fieldSize())]

    def cells(self):
        return [Cell() for i in range(self.fieldSize() ** 2)]

    @check(allBombed)
    @check(bombBombed)
    def isGameOver(self, player):
        return False

    def nextLevel(self):
        return "default"

    def name(self):
        return "nuclearlevel"
 
LevelsFactory.levels["nuclearlevel"] = Level()
