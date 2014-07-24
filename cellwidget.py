import kivy

from kivy.uix.button import Button
from kivy.properties import StringProperty

import weakref

class CellWidget(Button):
    """One cell widget"""
    def __init__(self, game, cell, field, **kwargs):
        super(CellWidget, self).__init__(**kwargs)
        self.cell = cell
        self.field = field
        self.cell.stateObservers.append(weakref.proxy(self))
        self.game = game
        self.bind(on_press = self.onPress)

    def onPress(self, e):
        self.game.pushOn(self.cell, self.field)

    def onCellStateChanged(self, state):
        images = {
            "empty": "images/empty_cell.png",
            "unit": "images/ship.png",
            "default": "images/cell.png",
            "checked": "images/checked_cell.png",
            "X": "images/bad_cell.png",
        }
        #self.text = state
        self.background_normal = images[state]


