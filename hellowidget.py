from kivy.uix.widget import Widget
from kivy.properties import StringProperty

from kivy.clock import Clock 

import weakref
import sys 

class HelloWidget(Widget):
    """Main widget"""
    
    class CB:
        """ Callback which hide the titles""" 
        def __init__(self, widget):
            self.widget = widget
        def __call__(self, *args, **kwargs):
            self.widget.game.update()
 
    def __init__(self, game, observer, **kwargs):
        super(HelloWidget, self).__init__(**kwargs)
        self.game = weakref.proxy(game)
        self.observer = weakref.proxy(observer)
        Clock.schedule_once(self.CB(self), 1)

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
 
    def onFieldSizeChanged(self, size):
        pass

    def onUnitsCountChange(self, units):
        self.observer.units = units


