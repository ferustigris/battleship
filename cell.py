" Cells module"

import units

class Cell:
    def __init__(self):
        self.__state = units.defaultState
        self.__hidden = False

    def hide(self):
        """ State will be shown as default"""
        self.__hidden = True 

    def unhide(self):
        """ State will be shown as is"""
        self.__hidden = False

    def setUnit(self, unit):
        self.__state = unit
    
    def pushOn(self):
        self.__state = self.__state.transfer(self)

    @property
    def state(self):
        """Return name of current state"""
        if self.__hidden:
            return "default"
        return self.__state.name

