from kivy.core.audio import SoundLoader
from kivy.clock import Clock 
import random
import weakref

class CB:
    term = False
    def __init__(self, sound, timeout):
        self.sound = sound
        self.t = timeout
        Clock.schedule_once(self, self.t())

    def __call__(self, *args, **kwargs):
        if self.term:
            return
        self.sound.volume = 0
        self.sound.play()
        Clock.schedule_once(self, self.t())

class SoundDecorator:
    def __init__(self, sound, player):
        self.player = weakref.proxy(player)
        self.sound = sound
    def play(self):
        if self.player.muteOn:
            self.sound.play()

class MPlayer:
    __backgroundSounds = []
    __bombs = {}

    def __init__(self):
        self.muteOn = True
        self.__start = SoundDecorator(SoundLoader.load('sounds/alarm.wav'), self)
        self.__gameOver = SoundDecorator(SoundLoader.load('sounds/tube.wav'), self)
        self.__levelUp = SoundDecorator(SoundLoader.load('sounds/kolokol.wav'), self)
        self.__radio1 = SoundDecorator(SoundLoader.load('sounds/radio.wav'), self)
        self.__radio2 = SoundDecorator(SoundLoader.load('sounds/radio_base.wav'), self)
        self.__sonar = SoundDecorator(SoundLoader.load('sounds/sonar.wav'), self)
        self.__button = SoundDecorator(SoundLoader.load('sounds/button.wav'), self)
        self.__bombs['default_unit'] = SoundDecorator(SoundLoader.load('sounds/bomb2.wav'), self)
        self.__bombs['bomb_unit'] = SoundDecorator(SoundLoader.load('sounds/shut.wav'), self)
        self.__bombs['nuclear_bomb_unit'] = SoundDecorator(SoundLoader.load('sounds/bomb3.wav'), self)
        self.__bombs['biology_bomb_unit'] = SoundDecorator(SoundLoader.load('sounds/sirena.wav'), self)
        self.__bombs['empty'] = SoundDecorator(SoundLoader.load('sounds/drip.wav'), self)

    def playMusic(self):
        self.__backgroundSounds.append(CB(self.__sonar, lambda : 5))
        self.__backgroundSounds.append(CB(self.__radio1, lambda : random.randint(10, 60)))
        self.__backgroundSounds.append(CB(self.__radio2, lambda : random.randint(10, 60)))

    def stopMusic(self):
        for sound in self.__backgroundSounds:
            sound.term = True

    def gameOver(self):
        self.__gameOver.play()

    def levelUp(self):
        self.__levelUp.play()

    def startGame(self):
        self.__start.play()

    def destroyUnit(self, unit):
        self.__bombs[unit].play()

    def setUnit(self, unit):
        self.__button.play()

    def turnSoundOn(self, on):
        self.muteOn = on

mplayer = MPlayer()

