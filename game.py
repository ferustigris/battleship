from fields import PlayerField

import weakref
import gamestates
from ai import AI, Player 
from levels import LevelsFactory

class Game:
    def __init__(self, gameStatesObserver):
        self.lvl = LevelsFactory().create("default")

        self.observer = gameStatesObserver
        self.state = gamestates.createInitState(self)

    def initPlayers(self):
        lvl = self.lvl
        
        self.players = [Player(lvl.units()), AI(lvl.units())]
        self.fields = [PlayerField(player, lvl.cells()) for player in self.players]

    def pushOn(self, cell, field):
        self.state.pushOn(self, cell, field)

    def update(self):
        for player, alienField in zip(self.players, self.fields[::-1]):
            player.update(alienField)
        self.state.update(self)

    def isGameOver(self):
        return self.lvl.isGameOver(self.players)

    def isReadyToPlay(self):
        return reduce(lambda r, player: r and player.isReadyToPlay(), self.players, True)
