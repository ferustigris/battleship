from levels import AbstractLevel, LevelsFactory, check

def bombBombed(self, player):
    """ Check, is bomb was bombed """
    return "nuclear_bomb_unit" in player.units

def allBombed(self, player):
    """ Check, is all players units are bombed """
    return player.units.count('default_unit') == self.fieldSize()

class Level(AbstractLevel):
    def fieldSize(self):
        return 5 

    def units(self):
        return ["nuclear_bomb_unit"] + ["default_unit" for i in range(self.fieldSize())]

    @check(allBombed)
    @check(bombBombed)
    def isGameOver(self, player):
        return False

    def nextLevel(self):
        return "biologylevel"

    def name(self):
        return "nuclearlevel"
 
LevelsFactory.levels["nuclearlevel"] = Level()
import biologylevel 
