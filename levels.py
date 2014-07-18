from abc import abstractmethod

class AbstractLevel:
    @abstractmethod
    def fieldSize(self):
        pass 
    @abstractmethod
    def units(self):
        pass 
    @abstractmethod
    def cells(self):
        pass 

def createDefault():
    from simplelevel import Level
    return Level()

