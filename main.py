import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock 

from game import Game
import weakref

class CellWidget(Button):
    """One cell widget"""
    def __init__(self, game, cell, **kwargs):
        super(CellWidget, self).__init__(**kwargs)
        self.cell = cell
        self.cell.stateObserver = weakref.proxy(self)
        self.game = game
        self.bind(on_press = self.onPress)

    def onPress(self, e):
        self.game.pushOn(self.cell)

    def onCellStateChanged(self):
        self.text = self.cell.state

class OceanGame(Widget):
    """Main widget"""
    text = StringProperty("")
    class CB:
        """ Callback which hide the titles""" 
        def __init__(self, widget):
            self.widget = widget
        def __call__(self, *args, **kwargs):
            self.widget.text = ""
 
    def __init__(self, **kwargs):
        super(OceanGame, self).__init__(**kwargs)

    def onGameStart(self, game):
        self.text = "Start"
        Clock.schedule_once(self.CB(self), 1)

    def onGamePrepare(self, game):
        self.text = "Arrange your units"
        Clock.schedule_once(self.CB(self), 1)



class OceanApp(App):
    def build(self):
        gameMainWidget = OceanGame()
        game = Game(gameMainWidget)

        for field, player in zip(gameMainWidget.fields, game.players):
            for cell in player.cells:
                field.add_widget(CellWidget(game, cell, text=cell.state))
        return gameMainWidget


if __name__ == '__main__':
    OceanApp().run()

