from cell import Cell

class PlayerField(object):
    active = False 
    def __init__(self, player, n):
        self.player = player
        self.cells = [Cell(i % n, i/n) for i in range(n ** 2)]
        player.cells = self.cells # is used by levels 
        
        for cell in self.cells:
            cell.stateObservers.append(player)

    def pushOn(self, game, cell):
        if self.active:
            if self.player.pushOn(game, cell):
                self.deactivate()

    def setUnit(self, cell):
        self.player.setUnitManual(self, cell)
        x, y = cell.x, cell.y
        koords = map(lambda i, j: (x + i, y + j), [0, 0, -1, 1], [-1, 1, 0, 0])
        cells = filter(lambda cell: (cell.x, cell.y) in koords, self.cells)
        [cell.deactivate() for cell in cells]

    def update(self, enemy):
        self.update = self.gameUpdate
        self.player.arrange(self.cells, self)

    def gameUpdate(self, enemy):
        if self.player.update(enemy.cells):
            self.activate()
    
    def activate(self):
        self.active = True
        [cell.activate() for cell in self.cells]

    def deactivate(self):
        self.active = False
        [cell.deactivate() for cell in self.cells]
