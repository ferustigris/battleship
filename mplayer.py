from kivy.core.audio import SoundLoader

class MPlayer:
    __startSound = SoundLoader.load('sounds/tube.wav')
    __backgroundSound = SoundLoader.load('sounds/beach.wav')

    def playMusic(self):
        self.__backgroundSound.loop = True;
        self.__backgroundSound.play()

    def stopMusic(self):
        self.__backgroundSound.loop = False;

    def startGame(self):
        self.__startSound.play()

mplayer = MPlayer()
