from levels import AbstractLevel, LevelsFactory, check
import random

def allBombed(self, player):
    """ Check, is all players units are bombed """
    return player.units.count('default_unit') == self.fieldSize()

class Level(AbstractLevel):
    def fieldSize(self):
        return 5 

    def units(self):
        return ["bomb_unit"] + ["default_unit" for i in range(self.fieldSize())]

    @check(allBombed)
    def isGameOver(self, player):
        return False

    def nextLevel(self):
        return "nuclearlevel"

    def name(self):
        return "bomblevel"

    def onBombed(self, player, cell, enemy):
        unit = cell.decorators["unit_type"]
        if unit == 'bomb_unit':
            koords = player.getNealestKoords(cell.x, cell.y)
            cells = filter(lambda cell: (cell.x, cell.y) in koords, player.cells)
            [cell.pushOn() for cell in cells]

LevelsFactory.levels["bomblevel"] = Level()
import nuclearlevel 
