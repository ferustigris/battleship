from levels import AbstractLevel, LevelsFactory, check

from cell import Cell
import cellstates 
import nuclearlevel 

def bombBombed(self, player):
    """ Check, is bomb was bombed """
    return "bomb_unit" in player.units

def allBombed(self, player):
    """ Check, is all players units are bombed """
    return  player.bombed == self.fieldSize()

class Level(AbstractLevel):
    def fieldSize(self):
        return 5 

    def units(self):
        return ["bomb_unit"] + ["default_unit" for i in range(self.fieldSize())]

    def cells(self):
        return [Cell() for i in range(self.fieldSize() ** 2)]

    @check(allBombed)
    @check(bombBombed)
    def isGameOver(self, player):
        return False

    def nextLevel(self):
        return "nuclearlevel"

    def name(self):
        return "bomblevel"
 
LevelsFactory.levels["bomblevel"] = Level()
