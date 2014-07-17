"""Units types"""

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
    """Unit has been bombed already"""
    def transfer(self, cell):
        return self

    @property
    def name(self):
        return "X"

class EmptyCellState(AbstractCellState):
    """Just empty"""
    def transfer(self, cell):
        cell.unhide()
        return CheckedEmptyCellState()

    @property
    def name(self):
        return "empty"

class CheckedEmptyCellState(EmptyCellState):
    """Empty cell is checked"""
    def transfer(self, cell):
        return self

    @property
    def name(self):
        return "checked" 

class UnitCellState(AbstractCellState):
    """Unit are there"""
    def transfer(self, cell):
        cell.unhide()
        return BombedCellState()

    @property
    def name(self):
        return "unit"

defaultState = EmptyCellState()
