from fields import PlayerField

import weakref
import gamestates
from ai import AI, Player 
from levels import LevelsFactory
from mplayer import mplayer 
from kivy.storage.jsonstore import JsonStore

class Game:
    store = JsonStore('battleship.json')
    score = 0
    sound = True

    def __init__(self, gameStatesObserver):
        levelName = "default"
        if self.store.exists('game'):
            gm = self.store.get('game')
            self.score = gm['score']
            levelName = gm['level']

        self.levelsFactory = LevelsFactory()
        self.lvl = self.levelsFactory.create(levelName)

        if self.store.exists('game'):
            self.onSound(gm['sound'])

        self.observer = gameStatesObserver
        self.observer.onGameInit(self)
        self.state = gamestates.createInitState(self)

    def initPlayers(self):
        lvl = self.lvl

        n = lvl.fieldSize()
        self.observer.onFieldSizeChanged(n)
        
        self.human = Player(lvl.units(), self)
        self.ai = AI(lvl.units(), self)
        self.humanField = PlayerField(self.human, n)
        self.aiField = PlayerField(self.ai, n)

    def pushOn(self, cell, field):
        self.state.pushOn(self, cell, field)

    def update(self):
        self.humanField.update(self.aiField)
        self.aiField.update(self.humanField)
        self.state.update(self)

    def isGameOver(self):
        return self.lvl.isGameOver(self.human)

    def isLevelUp(self):
        return self.lvl.isGameOver(self.ai)

    def isReadyToPlay(self):
        if self.human.isReadyToPlay():
            self.humanField.deactivate()
            self.aiField.activate()
            return True
        return False 

    def onUnitsCountChange(self, units):
        self.observer.onUnitsCountChange(units)

    def onScore(self, bonus):
        self.score += bonus
        self.observer.onScoreChanged(self.score)
        self.save()

    def onLevelUp(self, level):
        self.lvl = level
        self.save()

    def onBombed(self, player, cell):
        enemy = self.human if player == self.ai else self.ai
        self.lvl.onBombed(player, cell, enemy)
    
    def onSound(self, on):
        self.sound = on
        mplayer.turnSoundOn(self.sound)
        self.save()

    def fields(self):
        return [self.humanField, self.aiField]

    def save(self):
        """ Save game params into storage """
        self.store.put('game', level=self.lvl.name(), score=self.score, sound=self.sound)

