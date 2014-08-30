from cell import Cell

class PlayerField(object):
    active = True
    def __init__(self, player, n):
        self.player = player
        self.cells = [Cell(i % n, i/n) for i in range(n ** 2)]
        player.cells = self.cells # is used by levels 
        
        for cell in self.cells:
            cell.stateObservers.append(player)
        player.arrange(self.cells)

    def pushOn(self, game, cell):
        if self.active:
            self.player.pushOn(game, cell)
            self.active = False

    def setUnit(self, cell):
        self.player.setUnitManual(0, cell)

    def update(self, enemy):
        self.player.update(enemy.cells)
        self.active = True


