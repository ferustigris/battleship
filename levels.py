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

    @abstractmethod
    def nextLevel(self):
        return "default"

    @abstractmethod
    def name(self):
        return "default"

def check(condition):
    """ Decorators factory for check game over conditions"""
    def checkDecorator(func):
        """ Decorator. Check condition first and original function second """
        def checkCondition(self, player):
            return condition(self, player) or func(self, player)
        return checkCondition
    return checkDecorator 

class LevelsFactory:
    levels = {}
    nextLevel = "default"

    def __init__(self):
        import simplelevel

    def create(self, levelName):
        if levelName in self.levels.keys():
            return self.levels[levelName]

        return self.levels["default"]

    def next(self, currentLevel):
        return self.levels[currentLevel.nextLevel()]

