import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

from cell import Cell

class CellWidget(Button):
     def __init__(self, cell, **kwargs):
        super(CellWidget, self).__init__(**kwargs)
        self.cell = cell

     def onPress(self, e):
        self.text = self.cell.state

class OceanGame(Widget):
    text = StringProperty("Text 1")

    def __init__(self, cells, **kwargs):
        super(OceanGame, self).__init__(**kwargs)
        self.cells = cells

class OceanApp(App):
    def build(self):
        cells = []
        game = OceanGame(cells)

        for field in game.fields:
            for i in range(25):
                cell = Cell()
                cells.append(cell)
                btn1 = CellWidget(cell, text="0")
                btn1.bind(on_press=btn1.onPress)
                field.add_widget(btn1)
        return game


if __name__ == '__main__':
    OceanApp().run()

