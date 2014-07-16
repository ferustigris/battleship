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
    
class BombedCellState(AbstractCellState):
    def transfer(self, cell):
        return self

    @property
    def name(self):
        return "X"

class EmptyCellState(AbstractCellState):
    def transfer(self, cell):
        cell.unhide()
        return self

    @property
    def name(self):
        return "empty"

class UnitCellState(AbstractCellState):
    def transfer(self, cell):
        cell.unhide()
        return BombedCellState()

    @property
    def name(self):
        return "unit"


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
        self.__state = UnitCellState()
    
    def check(self):
        self.__state = self.__state.transfer(self)

    @property
    def state(self):
        """Return name of current state"""
        if self.__hidden:
            return "default"
        return self.__state.name

