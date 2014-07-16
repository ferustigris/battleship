" Cells module"

from abc import ABCMeta, abstractmethod

class AbstractCellState(object):
    """Abstract cell class"""
    @abstractmethod
    def transfer(self, cell):
        """ Transfer to next state"""
        pass

    @property
    @abstractmethod
    def name(self): 
        """ Return state name"""
        pass
    

class EmptyCellState(AbstractCellState):
    def __init__(self):
        pass
    def transfer(self, cell):
        pass

    @property
    def name(self):
        return "empty"

class Cell:
    def __init__(self):
        self.__state = EmptyCellState()
        self.__hidden = False

    def hide(self):
        """ State will be shown as default"""
        self.__hidden = True 

    def unhide(self):
        """ State will be shown as is"""
        self.__hidden = False

    def setUnit(self):
        self.__state.transfer(self)
    
    def check(self):
        self.__state.transfer(self)

    @property
    def state(self):
        """Return name of current state"""
        if self.__hidden:
            return "default"
        return self.__state.name

