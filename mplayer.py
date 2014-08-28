from kivy.core.audio import SoundLoader
from kivy.clock import Clock 
import random

class CB:
    term = False
    def __init__(self, sound, timeout):
        self.sound = sound
        self.t = timeout
        Clock.schedule_once(self, self.t())

    def __call__(self, *args, **kwargs):
        if self.term:
            return
        self.sound.play()
        Clock.schedule_once(self, self.t())

class MPlayer:
    __start = SoundLoader.load('sounds/alarm.wav')
    __radio1 = SoundLoader.load('sounds/radio.wav')
    __radio2 = SoundLoader.load('sounds/radio_base.wav')
    __sonar = SoundLoader.load('sounds/sonar.wav')

    __sonars = []

    def playMusic(self):
        self.__sonars.append(CB(self.__sonar, lambda : 5))
        self.__sonars.append(CB(self.__radio1, lambda : random.randint(10, 60)))
        self.__sonars.append(CB(self.__radio2, lambda : random.randint(10, 60)))

    def stopMusic(self):
        for sound in self.__sonars:
            sound.term = True

    def startGame(self):
        self.__start.play()

mplayer = MPlayer()
