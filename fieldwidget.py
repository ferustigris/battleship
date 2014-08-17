from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock 

from cellwidget import CellWidget

class FieldWidget(Widget):
    """Main widget"""
    text = StringProperty("")
    score = NumericProperty(353)
    defaultUnits = NumericProperty(0)
    bombs = NumericProperty(0)
    fieldSize = NumericProperty(5)

    missile = NumericProperty(0)
    missile_biology = NumericProperty(0)
    missile_nuk = NumericProperty(0)
    class CB:
        """ Callback which hide the titles""" 
        def __init__(self, widget):
            self.widget = widget
        def __call__(self, *args, **kwargs):
            self.widget.text = ""
 
    def __init__(self, **kwargs):
        super(FieldWidget, self).__init__(**kwargs)

    def onGameStart(self, game):
        self.showMessage("Start", 1)

    def onGameOver(self, game):
        self.showMessage("Game over", 2)

    def onGamePrepare(self, game):
        for field, fieldWidget in zip(self.fields, game.fields):
            field.clear_widgets()
            for cell in fieldWidget.cells:
                field.add_widget(CellWidget(game, cell, fieldWidget))
        self.showMessage("Arrange", 1)

    def onGameInit(self, game):
        pass

    def onUnitsCountChange(self, units):
        self.defaultUnits = units.count("default_unit")
        self.bombs = units.count("bomb_unit")

    def showMessage(self, text, timeout):
        self.text = text 
        Clock.schedule_once(self.CB(self), timeout)

    def onFieldSizeChanged(self, size):
        self.fieldSize = size

