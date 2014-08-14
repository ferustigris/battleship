from levels import AbstractLevel, LevelsFactory

from cell import Cell
import cellstates 

class Level(AbstractLevel):
    def fieldSize(self):
        return 5 

    def units(self):
        return ["bomb_unit"] + ["default_unit" for i in range(self.fieldSize())]

    def cells(self):
        return [Cell() for i in range(self.fieldSize() ** 2)]

    def isGameOver(self, players):
        for player in players:
            if player.bombed == self.fieldSize():
                return True
            if "bomb_unit" in player.units:
                return True
        return False

    def nextLevel(self):
        # import simplelevel 
        return "default"

 
LevelsFactory.levels["bomblevel"] = Level()
