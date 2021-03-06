" Cells module"

import cellstates 

class AbstractStateObserver:
    def onCellStateChanged(self, state):
        pass

class Cell:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.__state = cellstates.defaultState
        self.__hidden = False
        self.deactivated = False
        self.stateObservers = []
        self.activeObservers = []
        self.decorators = {}

    def deactivate(self):
        self.deactivated = True 
        for observer in self.activeObservers:
            observer.onDeactivated()

    def activate(self):
        self.deactivated = False
        for observer in self.activeObservers:
            observer.onActivated()

    def addActivateObserver(self, observer):
        if self.deactivated:
            observer.onDeactivated()
        self.activeObservers.append(observer)

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

