from fields import PlayerField

import weakref
import gamestates
from ai import AI 
from levels import LevelsFactory

class Game:
    def __init__(self, gameStatesObserver):
        self.lvl = LevelsFactory().create("default")

        self.observer = weakref.proxy(gameStatesObserver)
        self.state = gamestates.createInitState(self)

    def initPlayers(self):
        lvl = self.lvl
        
        self.ai = AI()
        self.player = PlayerField(lvl.cells(), lvl.units())
        self.pc = PlayerField(lvl.cells(), lvl.units())
        
        self.fields = [self.player, self.pc]
        self.ai.arrange(self.pc)

    def pushOn(self, cell):
        self.state.pushOn(self, cell)

    def update(self):
        self.ai.update(self)
        self.state.update(self)

