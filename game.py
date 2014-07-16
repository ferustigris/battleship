from cell import Cell
from fields import PlayerField, ComputerField

class Game:
    def __init__(self):
        self.gameSize = 5

        player = PlayerField([Cell() for i in range(self.gameSize ** 2)])
        pc = ComputerField([Cell() for i in range(self.gameSize ** 2)])
        
        self.players = [player, pc]
 
        for player in game.players:
            player.arrange()
 

