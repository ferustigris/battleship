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

from kivy.clock import Clock 

class EmptyCellState(AbstractCellState):
    """Just empty"""
    def transfer(self, cell):
        cell.unhide()
        return LazyCellState(CheckedEmptyCellState(), cell)

    @property
    def name(self):
        return "empty" 

class LazyCellState(EmptyCellState):
    """Empty cell is checked"""
    class CB:
        """ Callback which hide the titles""" 
        def __init__(self, cell, newState):
            self.cell = cell 
            self.newState = newState 
        def __call__(self, *args, **kwargs):
            self.cell.setState(self.newState)

    def __init__(self, nextState, cell):
        Clock.schedule_once(self.CB(cell, nextState), 1)

    def transfer(self, cell):
        return self

    @property
    def name(self):
        return "on_step" 

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
        return LazyCellState(BombedCellState(), cell)

    @property
    def name(self):
        return "unit"

defaultState = EmptyCellState()
