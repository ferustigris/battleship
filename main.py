import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App

from game import Game
from fieldwidget import FieldWidget

import weakref

class OceanApp(App):
    '''Main appliaction class'''
    def build(self):
        gameMainWidget = FieldWidget()
        game = Game(gameStatesObserver=gameMainWidget)
        
        gameMainWidget.game = game
        gameMainWidget.onGameInit(game)

        return gameMainWidget


if __name__ == '__main__':
    OceanApp().run()

