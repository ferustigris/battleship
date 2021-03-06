"""Game states"""

from abc import ABCMeta, abstractmethod
from mplayer import mplayer 

class AbstractGameState:
    @abstractmethod
    def pushOn(self, game, cell, field):
        pass

    @abstractmethod
    def update(self, game):
        pass

class PlayGameState(AbstractGameState):
    def __init__(self):
        mplayer.startGame()
        mplayer.playMusic()

    def pushOn(self, game, cell, field):
        field.pushOn(game, cell)

    def update(self, game):
        if game.isGameOver():
            game.state = GameOverState()
            game.observer.onGameOver(game)
            mplayer.stopMusic() 
        if game.isLevelUp():
            game.onLevelUp(game.levelsFactory.next(game.lvl))

            game.state = GameLevelUp()
            game.observer.onLevelUp(game)
            mplayer.stopMusic() 

class GameOverState(AbstractGameState):
    def __init__(self):
        mplayer.gameOver()

    def pushOn(self, game, cell, field):
       game.state = InitGameState(game)
       game.observer.onGameInit(game)
    def update(self, game):
        pass

class GameLevelUp(AbstractGameState):
    def __init__(self):
        mplayer.levelUp()

    def pushOn(self, game, cell, field):
       game.state = InitGameState(game)
       game.observer.onGameInit(game)
    def update(self, game):
        pass

class InitGameState(AbstractGameState):
    def __init__(self, game):
       game.initPlayers()

    def pushOn(self, game, cell, field):
       game.state = PrepareGameState()
       game.observer.onGamePrepare(game)

    def update(self, game):
       game.state = PrepareGameState()
       game.observer.onGamePrepare(game) 

class PrepareGameState(AbstractGameState):
    def pushOn(self, game, cell, field):
        field.setUnit(cell)

        if game.isReadyToPlay():
            game.state = PlayGameState()
            game.observer.onGameStart(game)

    def update(self, game):
        pass

def createInitState(game):
    return InitGameState(game)

