import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

from game import Game

class CellWidget(Button):
     def __init__(self, game, cell, **kwargs):
        super(CellWidget, self).__init__(**kwargs)
        self.cell = cell
        self.game = game

     def onPress(self, e):
        self.game.pushOn(self.cell)
        self.text = self.cell.state

class OceanGame(Widget):
    text = StringProperty("Text 1")

    def __init__(self, cells, **kwargs):
        super(OceanGame, self).__init__(**kwargs)
        self.cells = cells

class OceanApp(App):
    def build(self):
        gameMainWidget = OceanGame([])
        game = Game()

        for field, player in zip(gameMainWidget.fields, game.players):
            for cell in player.cells:
                btn1 = CellWidget(game, cell, text=cell.state)
                btn1.bind(on_press=btn1.onPress)
                field.add_widget(btn1)
        return gameMainWidget


if __name__ == '__main__':
    OceanApp().run()

