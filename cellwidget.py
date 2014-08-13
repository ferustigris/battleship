import kivy

from kivy.uix.button import Button
from kivy.graphics import Rectangle
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

    def onCellStateChanged(self, cell, state):
        images = {
            "empty": "images/empty_cell.png",
            "unit": "images/unit.png",
            "checked": "images/checked_cell.png",
            "X": "images/bad_cell.png",
            "default": "images/cell.png",

            "default_unit": "images/ship.png",
        }

        if state != "default":
            with self.canvas.before:
                for type, decorator in cell.decorators.items():
                    Rectangle(source=images[decorator], pos=self.pos, size=self.size)

        self.background_normal = images[state]
