from kivy.uix.widget import Widget
from kivy.properties import StringProperty

import weakref
import sys 

class HelloWidget(Widget):
    """Main widget"""

    def __init__(self, game, observer, **kwargs):
        super(HelloWidget, self).__init__(**kwargs)
        self.game = weakref.proxy(game)
        self.observer = weakref.proxy(observer)

    def exitGame(self):
        sys.exit(0)      

    def startHumanVsAndroidGame(self):
        self.game.update()

    def startHumanVsHumanGame(self):
        self.game.update()

    def onGameStart(self, game):
        pass 

    def onGameOver(self, game):
        pass 

    def onGamePrepare(self, game):
        pass 

    def onGameInit(self, game):
        pass 
 
    def onUnitsCountChange(self, units):
        pass


