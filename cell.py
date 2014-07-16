" Cells module"

import units


class EmptyStateObserver:
    def onCellStateChanged(self):
        pass

class Cell:
    def __init__(self):
        self.__state = units.defaultState
        self.__hidden = False
        self.stateObserver = EmptyStateObserver()

    def hide(self):
        """ State will be shown as default"""
        self.__hidden = True 

    def unhide(self):
        """ State will be shown as is"""
        self.__hidden = False

    def setUnit(self, unit):
        self.setState(unit)
    
    def pushOn(self):
        self.setState(self.__state.transfer(self))

    @property
    def state(self):
        """Return name of current state"""
        if self.__hidden:
            return "default"
        return self.__state.name

    def setState(self, newState):
        self.__state = newState
        self.stateObserver.onCellStateChanged()
