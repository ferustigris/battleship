from abc import abstractmethod

class AbstractLevel:
    @abstractmethod
    def fieldSize(self):
        pass 

    @abstractmethod
    def units(self):
        pass 

    @abstractmethod
    def cells(self):
        pass 

    @abstractmethod
    def isGameOver(self, players):
        pass

class LevelsFactory:
    levels = {}
    def create(self, levelName):
        if levelName in self.levels.keys():
            return levels[levelName]

        from simplelevel import Level
        return Level()

