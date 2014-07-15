import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock

class CellWidget(Button):
    pass

class OceanGame(Widget):
    text = StringProperty("Text 1")

    def update(self, dt):
        pass
#        i += 1
        self.text = "Test 3"
    def on_touch_down(self, touch):
        pass


class OceanApp(App):

    def build(self):
        game = OceanGame()
        Clock.schedule_interval(game.update, 1.0/60.0)

        for i in range(25):
            game.fieldLeft.add_widget(CellWidget(text="0"))
            game.fieldRight.add_widget(CellWidget(text="0"))
        return game


if __name__ == '__main__':
    OceanApp().run()

