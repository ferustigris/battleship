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
        self.onBombedSized(player, cell, enemy, self.fieldSize())

    def onBombedSized(self, player, cell, enemy, n):
        unit = cell.decorators["unit_type"]
        if unit == 'bomb_unit':
            x = cell.x 
            y = cell.y 
            koords = map(lambda i, j: (x + i, y + j), [0, 0, -1, 1], [-1, 1, 0, 0])
            koords = filter(lambda(x, y): 0 <= x < n and 0 <= y < n, koords)# remove unbounded
            cells = filter(lambda cell: (cell.x, cell.y) in koords, player.cells)
            [cell.pushOn() for cell in cells]

LevelsFactory.levels["bomblevel"] = Level()
import nuclearlevel 
