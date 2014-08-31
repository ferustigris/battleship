from levels import AbstractLevel, LevelsFactory, check

def allBombed(self, player):
    """ Check, is all players units are bombed """
    return player.units.count('default_unit') == self.fieldSize()

class Level(AbstractLevel):
    def __init__(self, bombsCount, biologiesCount, size):
        self.bombsCount = bombsCount
        self.biologiesCount = biologiesCount
        self.size = size
        lvls = LevelsFactory()
        self.__bombLevel = lvls.create('bomblevel')
        self.__bombLevel.fieldSize = lambda : size
        self.__biologyLevel = lvls.create('biologylevel')

    def fieldSize(self):
        return self.size

    def units(self):
        return ["bomb_unit" for i in range(self.bombsCount)] + ["biology_bomb_unit" for i in
                range(self.biologiesCount)] + ["default_unit" for i in range(self.fieldSize())]

    @check(allBombed)
    def isGameOver(self, player):
        return self.__biologyLevel.isGameOver(player) or self.__bombLevel.isGameOver(player)

    def nextLevel(self):
        return "default" if self.name() == "extrabomblevel_5_4_8" else self.formatName(self.bombsCount + 1, self.biologiesCount + 1, self.size + 1)

    def name(self):
        return self.formatName(self.bombsCount, self.biologiesCount, self.size)

    def formatName(self, bombsCount, biologiesCount, size):
        return "extrabomblevel_" +  str(bombsCount) + "_" +  str(biologiesCount) + "_" +  str(size)

    def onBombed(self, player, cell, enemy):
        self.__biologyLevel.onBombed(player, cell, enemy)
        self.__bombLevel.onBombedSized(player, cell, enemy, self.size)

for i,j,c in map(None , range(1, 6), range(0, 5), range(4, 9)):
    lvl = Level(i, j, c)
    LevelsFactory.levels[lvl.name()] = lvl
