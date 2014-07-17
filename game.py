from fields import PlayerField, ComputerField

import weakref
import gamestates
from ai import AI 
from levels import Level

class Game:
    def __init__(self, gameStatesObserver):
        self.lvl = Level()

        self.observer = weakref.proxy(gameStatesObserver)
        self.state = gamestates.createInitState(self)

    def initPlayers(self):
        lvl = self.lvl
        
        self.ai = AI()
        self.player = PlayerField(lvl.cells(), lvl.units())
        self.pc = ComputerField(lvl.cells(), lvl.units())
        
        self.players = [self.player, self.pc]
        self.ai.arrange(self.pc)

    def pushOn(self, cell):
        self.state.pushOn(self, cell)

    def update(self):
        self.ai.update(self)
        self.state.update(self)

