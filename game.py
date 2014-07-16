from cell import Cell
from fields import PlayerField, ComputerField

import weakref
import gamestates
from ai import AI 

class Game:
    def __init__(self, gameStatesObserver):
        self.gameSize = 5

        self.player = PlayerField([Cell() for i in range(self.gameSize ** 2)])
        self.pc = ComputerField([Cell() for i in range(self.gameSize ** 2)])
        
        self.players = [self.player, self.pc]
 
        self.ai = AI()
        self.ai.arrange(self.pc)

        self.observer = weakref.proxy(gameStatesObserver)
        self.state = gamestates.initState

    def pushOn(self, cell):
        self.state.pushOn(self, cell)

    def update(self):
        self.ai.update(self)
        
