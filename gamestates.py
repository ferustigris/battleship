"""Game states"""

from abc import ABCMeta, abstractmethod

class AbstractGameState:
    @abstractmethod
    def pushOn(self, game, cell):
        pass
    @abstractmethod
    def update(self, game):
        pass

class PlayGameState(AbstractGameState):
    def __init__(self):
        self.steps = []
    def pushOn(self, game, cell):
        if cell in game.pc.cells and cell not in self.steps:
            cell.pushOn()
            game.update()
            self.steps.append(cell)
    def update(self, game):
        for player in game.players:
            if player.bombed == len(game.lvl.units()):
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
    def __init__(self):
        self.alive = []
    def pushOn(self, game, cell):
        if cell in game.player.cells and cell not in self.alive:
            cell.setUnit(game.player.freeUnits.pop())
            self.alive.append(cell)
            
        if not game.player.freeUnits:
            game.state = PlayGameState()
            game.observer.onGameStart(game)
    def update(self, game):
        pass

def createInitState(game):
    return InitGameState(game)
