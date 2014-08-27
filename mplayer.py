from kivy.core.audio import SoundLoader
from kivy.clock import Clock 
import random

class CB:
    def __init__(self, sound, timeout):
        self.sound = sound
        self.t = timeout
        Clock.schedule_once(self, self.t())

    def __call__(self, *args, **kwargs):
        self.sound.play()
        Clock.schedule_once(self, self.t())

class MPlayer:
    __startSound = SoundLoader.load('sounds/tube.wav')
    __radio1 = SoundLoader.load('sounds/radio.wav')
    __radio1 = SoundLoader.load('sounds/radio_base.wav')
    __backgroundSound = SoundLoader.load('sounds/sonar.wav')

    def playMusic(self):
        #self.__backgroundSound.loop = True;
        #self.__backgroundSound.play()
        CB(self.__backgroundSound, lambda : 5)
        CB(self.__radio1, lambda : random.randint(10, 60))
        CB(self.__radio2, lambda : random.randint(10, 60))

    def stopMusic(self):
        #self.__backgroundSound.loop = False;
        pass

    def startGame(self):
        self.__startSound.play()

mplayer = MPlayer()
