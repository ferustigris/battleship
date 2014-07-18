"""Game states"""

from abc import ABCMeta, abstractmethod

class AbstractGameState:
    @abstractmethod
    def pushOn(self, game, cell):
        pass
    @abstractmethod
    def update(self, game):
        pass

def CheckLastSteps(func):
    '''Step has been made'''
    steps = []
    def __CheckLastSteps(self, game, cell):
        if cell in steps:
            return None
        steps.append(cell)
        return func(self, game, cell)
    return __CheckLastSteps
    
class PlayGameState(AbstractGameState):
    @CheckLastSteps
    def pushOn(self, game, cell):
        for field in game.fields:
            field.pushOn(game, cell)

    def update(self, game):
        if game.isGameOver():
            game.state = GameOverState()
            game.observer.onGameOver(game)


class GameOverState(AbstractGameState):
    def pushOn(self, game, cell):
       game.state = InitGameState(game)
       game.observer.onGameInit(game)
    def update(self, game):
        pass

class InitGameState(AbstractGameState):
    def __init__(self, game):
        game.initPlayers()
    def pushOn(self, game, cell):
       game.state = PrepareGameState()
       game.observer.onGamePrepare(game) 
    def update(self, game):
        pass

class PrepareGameState(AbstractGameState):
    @CheckLastSteps
    def pushOn(self, game, cell):
        for field in game.fields:
            field.setUnit(cell)

        if game.isReadyToPlay():
            game.state = PlayGameState()
            game.observer.onGameStart(game)
    def update(self, game):
        pass

def createInitState(game):
    return InitGameState(game)
