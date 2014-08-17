from fields import PlayerField

import weakref
import gamestates
from ai import AI, Player 
from levels import LevelsFactory

class Game:
    def __init__(self, gameStatesObserver):
        self.levelsFactory = LevelsFactory()
        self.lvl = self.levelsFactory.create("default")

        self.observer = gameStatesObserver
        self.observer.onGameInit(self)
        self.state = gamestates.createInitState(self)

    def initPlayers(self):
        lvl = self.lvl
        
        self.players = [Player(lvl.units(), self, lvl.cells()), AI(lvl.units(), self, lvl.cells())]
        self.fields = [PlayerField(player) for player in self.players]

    def pushOn(self, cell, field):
        self.state.pushOn(self, cell, field)

    def update(self):
        for player in self.players:
            for alien in filter(lambda r: not (r == player), self.players):
                player.update(alien)
        self.state.update(self)

    def isGameOver(self):
        if self.lvl.isGameOver(self.players):
            self.lvl = self.levelsFactory.next(self.lvl)
            self.onserver.onFieldSizeChanged(self.lvl.fieldSize())
            return True
        return False

    def isReadyToPlay(self):
        return reduce(lambda r, player: r and player.isReadyToPlay(), self.players, True)

    def onUnitsCountChange(self, units):
        self.observer.onUnitsCountChange(units)

