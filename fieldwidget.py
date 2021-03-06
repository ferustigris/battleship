from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.clock import Clock 
import weakref 
from cellwidget import CellWidget

class FieldWidget(Widget):
    """Main widget"""
    sound = BooleanProperty(True)
    text = StringProperty("")
    score = NumericProperty(0)
    defaultUnits = NumericProperty(0)
    bombs = NumericProperty(0)
    fieldSize = NumericProperty(5)

    biology_bombs = NumericProperty(0)
    nuclear_bombs = NumericProperty(0)

    
    class CB:
        """ Callback which hide the titles""" 
        def __init__(self, widget):
            self.widget = widget
        def __call__(self, *args, **kwargs):
            self.widget.text = ""
 
    def __init__(self, game, **kwargs):
        super(FieldWidget, self).__init__(**kwargs)
        self.game = weakref.proxy(game)
        self.sound = game.sound

    def onGameStart(self, game):
        self.showMessage("start", 1)

    def onLevelUp(self, game):
        self.showMessage("Level up", 2)

    def onGameOver(self, game):
        self.showMessage("Game over", 2)

    def onGamePrepare(self, game):
        self.score = game.score
        for field, fieldWidget in zip(self.fields, game.fields()):
            field.clear_widgets()
            for cell in fieldWidget.cells:
                field.add_widget(CellWidget(game, cell, fieldWidget))
        self.showMessage("Arrange", 1)

    def onGameInit(self, game):
        pass

    def onUnitsCountChange(self, units):
        self.defaultUnits = units.count("default_unit")
        self.bombs = units.count("bomb_unit")
        self.nuclear_bombs = units.count("nuclear_bomb_unit")
        self.biology_bombs = units.count("biology_bomb_unit")

    def showMessage(self, text, timeout):
        self.text = text 
        Clock.schedule_once(self.CB(self), timeout)

    def onFieldSizeChanged(self, size):
        self.fieldSize = size

    def onScoreChanged(self, score):
        self.score = score
        #self.showMessage(str(bonus), 1) # TODO: make clouds with added bonuses

    def turnSoundOn(self, on):
        self.sound = on
        self.game.onSound(self.sound)

