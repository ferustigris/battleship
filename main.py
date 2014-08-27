import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App

from game import Game
from fieldwidget import FieldWidget
from hellowidget import HelloWidget
from kivy.uix.widget import Widget

import weakref

class RootWidget(Widget):
    pass

class UnitWidget(Widget):
    pass

class GameStatesObserver:
    def __init__(self, RootWidget):
        self.RootWidget = RootWidget
        self.units = []

    def onGameStart(self, game):
        self.current.onGameStart(game)

    def onGameOver(self, game):
        self.current.onGameOver(game)

    def onLevelUp(self, game):
        self.current.onLevelUp(game)

    def onGamePrepare(self, game):
        self.RootWidget.rootLayout.clear_widgets()
        self.current = FieldWidget()

        self.current.onUnitsCountChange(self.units)
        self.units = []

        self.current.onGamePrepare(game)
        self.RootWidget.rootLayout.add_widget(self.current)

    def onGameInit(self, game):
        self.RootWidget.rootLayout.clear_widgets()
        self.current = HelloWidget(game, self)
        self.current.onGameInit(game)
        self.RootWidget.rootLayout.add_widget(self.current)

    def onUnitsCountChange(self, units):
        self.current.onUnitsCountChange(units)

    def onFieldSizeChanged(self, size):
        self.current.onFieldSizeChanged(size)

    def onScoreChanged(self, bonus):
        self.current.onScoreChanged(bonus)

class OceanApp(App):
    '''Main appliaction class'''
    def build(self):
        rootWidget = RootWidget()
        observer = GameStatesObserver(rootWidget)
        rootWidget.game = Game(gameStatesObserver=observer)
        return rootWidget

if __name__ == '__main__':
    OceanApp().run()

