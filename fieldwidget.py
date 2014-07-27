from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock 

from cellwidget import CellWidget

class FieldWidget(Widget):
    """Main widget"""
    text = StringProperty("")
    score = StringProperty("353")
    units = StringProperty("")
    class CB:
        """ Callback which hide the titles""" 
        def __init__(self, widget):
            self.widget = widget
        def __call__(self, *args, **kwargs):
            self.widget.text = ""
 
    def __init__(self, **kwargs):
        super(FieldWidget, self).__init__(**kwargs)

    def onGameStart(self, game):
        self.text = "Start"
        Clock.schedule_once(self.CB(self), 1)

    def onGameOver(self, game):
        self.text = "Game over"
        Clock.schedule_once(self.CB(self), 2)

    def onGamePrepare(self, game):
        for field, fieldWidget in zip(self.fields, game.fields):
            field.clear_widgets()
            for cell in fieldWidget.cells:
                field.add_widget(CellWidget(game, cell, fieldWidget))

        self.text = "Arrange your units"
        Clock.schedule_once(self.CB(self), 1)

    def onGameInit(self, game):
        pass

    def onUnitsCountChange(self, units):
        self.units = str(len(units))

