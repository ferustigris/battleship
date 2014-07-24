
import weakref

class PlayerField(object):
    def __init__(self, player, cells):
        player.field = weakref.proxy(self)
        self.player = player
        self.cells = cells
        for cell in cells:
            cell.stateObservers.append(player)
        player.arrange()

    def pushOn(self, game, cell):
        if cell in self.cells:
            self.player.pushOn(game, cell)

    def setUnit(self, cell):
        if cell in self.cells:
            self.player.setUnitManual(cell)


