"""Game states"""

from abc import ABCMeta, abstractmethod

class AbstractGameState:
    @abstractmethod
    def pushOn(self, game, cell):
        pass

class WaitPlayGameState(AbstractGameState):
    def pushOn(self, game, cell):
       game.state = PlayGameState()


class PlayGameState(AbstractGameState):
    def pushOn(self, game, cell):
        if cell in game.pc.cells:
            cell.pushOn()
        game.update()

class InitGameState(AbstractGameState):
    def pushOn(self, game, cell):
       game.state = WaitPrepareGameState()
       game.observer.onGamePrepare(game) 

class WaitPrepareGameState(AbstractGameState):
    def pushOn(self, game, cell):
       game.state = PrepareGameState()

class PrepareGameState(AbstractGameState):
    def pushOn(self, game, cell):
        if cell in game.player.cells:
            cell.setUnit(game.player.freeUnits.pop())
            
        if not game.player.freeUnits:
            game.state = WaitPlayGameState()
            game.observer.onGameStart(game)


initState = InitGameState()
