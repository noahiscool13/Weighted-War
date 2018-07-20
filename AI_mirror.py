from Game import *


class AI(Player):
    def move(self, current, player):
        return current[-1]