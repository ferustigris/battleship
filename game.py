from cell import Cell
from fields import PlayerField, ComputerField
from abc import ABCMeta, abstractmethod

import weakref

class AbstractGameState:
    @abstractmethod
    def pushOn(self, game, cell):
        pass

class WaitPlayGameState(AbstractGameState):
    def pushOn(self, game, cell):
       game.state = PlayGameState()


class PlayGameState(AbstractGameState):
    def pushOn(self, game, cell):
        cell.pushOn()

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

class Game:
    def __init__(self, gameStatesObserver):
        self.gameSize = 5

        self.player = PlayerField([Cell() for i in range(self.gameSize ** 2)])
        self.pc = ComputerField([Cell() for i in range(self.gameSize ** 2)])
        
        self.players = [self.player, self.pc]
 
        for player in self.players:
            player.arrange()

        self.observer = weakref.proxy(gameStatesObserver)
        self.state = InitGameState()

    def pushOn(self, cell):
        self.state.pushOn(self, cell)

