import random

class AI:
    def __init__(self):
        self.lastSteps = []
        
    def update(self, game):
        allPossibleSteps = range(len(game.player.cells))
        steps = list(set(allPossibleSteps).difference(self.lastSteps))
        x = random.choice(steps)
        self.lastSteps.append(x)
        game.player.cells[x].pushOn()

    def arrange(self, player):
        for cell in player.cells:
            cell.hide()

        indexes = range(len(player.cells))
        while player.freeUnits:
            rInd = random.choice(indexes)
            indexes.remove(rInd)
            player.setUnit(rInd)

 
