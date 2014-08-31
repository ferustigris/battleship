from levels import AbstractLevel, LevelsFactory, check
import random

def allBombed(self, player):
    """ Check, is all players units are bombed """
    return player.units.count('default_unit') == self.fieldSize()

class Level(AbstractLevel):
    def fieldSize(self):
        return 5 

    def units(self):
        return ["biology_bomb_unit"] + ["default_unit" for i in range(self.fieldSize())]

    @check(allBombed)
    def isGameOver(self, player):
        return False

    def nextLevel(self):
        return "extrabomblevel_1_0_4"

    def name(self):
        return "biologylevel"
 
    def onBombed(self, player, cell, enemy):
        unit = cell.decorators["unit_type"]
        if unit == 'biology_bomb_unit':
            ship = random.choice(enemy.ships)
            ship.pushOn()

LevelsFactory.levels["biologylevel"] = Level()
import extrabomblevel 
