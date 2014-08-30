import kivy

from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.properties import StringProperty

import weakref

class CellWidget(Button):
    """One cell widget"""
    images = {
            "empty": "images/empty_cell.png",
            "unit": "images/unit.png",
            "checked": "images/checked_cell.png",
            "hidden": "images/unit.png",
            "X": "images/bad_cell.png",
            "default": "images/cell.png",

            "default_unit": "images/ship.png",
            "bomb_unit": "images/bomb.png",
            "nuclear_bomb_unit": "images/nuclear_bomb.png",
            "biology_bomb_unit": "images/biology_bomb.png",
            }
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
        self.redraw()

    def redraw(self):
        state = self.cell.state
        if state != "default" and state != "hidden":
            with self.canvas.before:
                for type, decorator in self.cell.decorators.items():
                    Rectangle(source=self.images[decorator], pos=self.pos, size=self.size)
        self.background_normal = self.images[state]
        self.background_down = self.images[state]

