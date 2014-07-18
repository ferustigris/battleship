
import weakref

class PlayerField(object):
    def __init__(self, player, cells, units):
        player.field = weakref.proxy(self)
        self.player = player
        self.cells = cells
        for cell in cells:
            cell.stateObservers.append(player)
        self.freeUnits = units 
        player.arrange(self)

    def pushOn(self, game, cell):
        if cell in self.cells:
            self.player.pushOn(game, cell)

    def setUnit(self, cell):
        if cell in self.cells:
            cell.setUnit(self.freeUnits.pop())
        return False


