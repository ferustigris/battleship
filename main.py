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

class GameStatesObserver:
    def __init__(self, root):
        self.root = root

    def onGameStart(self, game):
        self.current.onGameStart(game)

    def onGameOver(self, game):
        self.current.onGameOver(game)

    def onGamePrepare(self, game):
        self.root.rootLayout.clear_widgets()
        self.current = FieldWidget()
        self.current.onGamePrepare(game)
        self.root.rootLayout.add_widget(self.current)

    def onGameInit(self, game):
        self.root.rootLayout.clear_widgets()
        self.current = HelloWidget(game, self)
        self.current.onGameInit(game)
        self.root.rootLayout.add_widget(self.current)

class OceanApp(App):
    '''Main appliaction class'''
    def build(self):
        root = RootWidget()
        observer = GameStatesObserver(root)
        root.game = Game(gameStatesObserver=observer)
        observer.onGameInit(root.game)
        return root

if __name__ == '__main__':
    OceanApp().run()

