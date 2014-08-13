" Cells module"

import cellstates 

class AbstractStateObserver:
    def onCellStateChanged(self, state):
        pass

class Cell:
    def __init__(self):
        self.__state = cellstates.defaultState
        self.__hidden = False
        self.stateObservers = []
        self.decorators = {}

    def hide(self):
        """ State will be shown as default"""
        self.__hidden = True 

    def unhide(self):
        """ State will be shown as is"""
        self.__hidden = False

    def setUnit(self, unit):
        self.decorators["unit_type"] = unit
        self.setState(cellstates.UnitCellState())

    def pushOn(self):
        self.setState(self.__state.transfer(self))

    @property
    def state(self):
        """Return name of current state"""
        if self.__hidden:
            return "default"
        return self.__state.name

    def setState(self, newState):
        if self.__state == newState:
            return
        self.__state = newState
        for observer in self.stateObservers:
            observer.onCellStateChanged(self, self.state)

