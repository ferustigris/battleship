import random

class AI:
    def __init__(self):
        self.lastSteps = []
        
    def update(self, game):
        while True:
            x = random.randrange(len(game.player.cells))
            if x not in self.lastSteps:
                self.lastSteps.append(x)
                break
            if len(self.lastSteps) == len(game.player.cells):
                break
        game.player.cells[x].pushOn()

    def arrange(self, player):

        for cell in player.cells:
            cell.hide()

        while player.freeUnits:
            rInd = random.randrange(len(player.cells))
            player.cells[rInd].setUnit(player.freeUnits.pop())

 
