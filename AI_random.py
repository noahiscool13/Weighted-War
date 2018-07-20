from random import choice
from Game import *


class AI(Player):

    def move(self, current, player):
        game = self.current_game
        if player == 1:
            return choice(game.p_1_cards)
        return choice(game.p_2_cards)