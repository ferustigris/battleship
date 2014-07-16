from cell import Cell
from fields import PlayerField, ComputerField
from abc import ABCMeta, abstractmethod

class AbstractGameState:
    @abstractmethod
    def pushOn(self, game, cell):
        pass

class PlayGameState(AbstractGameState):
    def pushOn(self, game, cell):
        cell.check()

class PrepareGameState(AbstractGameState):
    def pushOn(self, game, cell):
        if cell in game.player.cells:
            cell.setUnit(game.player.freeUnits.pop())
            
        if not game.player.freeUnits:
            game.state = PlayGameState()

class Game:
    def __init__(self):
        self.gameSize = 5

        self.player = PlayerField([Cell() for i in range(self.gameSize ** 2)])
        self.pc = ComputerField([Cell() for i in range(self.gameSize ** 2)])
        
        self.players = [self.player, self.pc]
 
        for player in self.players:
            player.arrange()

        self.state = PrepareGameState()

    def pushOn(self, cell):
        self.state.pushOn(self, cell)

