from levels import AbstractLevel, LevelsFactory, check
import random

from cell import Cell
import cellstates 
import nuclearlevel 

def allBombed(self, player):
    """ Check, is all players units are bombed """
    return player.units.count('default_unit') == self.fieldSize()

class Level(AbstractLevel):
    def fieldSize(self):
        return 5 

    def units(self):
        return ["bomb_unit"] + ["default_unit" for i in range(self.fieldSize())]

    def cells(self):
        return [Cell() for i in range(self.fieldSize() ** 2)]

    @check(allBombed)
    def isGameOver(self, player):
        return False

    def nextLevel(self):
        return "nuclearlevel"

    def name(self):
        return "bomblevel"

    def onBombed(self, player, unit, enemy):
        if unit == 'bomb_unit':
            ship = random.choice(enemy.ships)
            ship.pushOn()

LevelsFactory.levels["bomblevel"] = Level()
