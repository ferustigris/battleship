
import weakref

class PlayerField(object):
    def __init__(self, player):
        player.field = weakref.proxy(self)
        self.player = player
        self.cells = player.cells
        
        for cell in self.player.cells:
            cell.stateObservers.append(player)
        player.arrange()

    def pushOn(self, game, cell):
        if cell in self.player.cells:
            self.player.pushOn(game, cell)

    def setUnit(self, cell):
        if cell in self.player.cells:
            self.player.setUnitManual(cell)


