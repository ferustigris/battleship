import kivy

from kivy.uix.button import Button
from kivy.properties import StringProperty

import weakref

class CellWidget(Button):
    """One cell widget"""
    def __init__(self, game, cell, **kwargs):
        super(CellWidget, self).__init__(**kwargs)
        self.cell = cell
        self.cell.stateObservers.append(weakref.proxy(self))
        self.game = game
        self.bind(on_press = self.onPress)

    def onPress(self, e):
        self.game.pushOn(self.cell)

    def onCellStateChanged(self, state):
        self.text = state


