class Game:
    def __init__(self):
        p_1_cards = list(range(1, 11))
        p_2_cards = list(range(1, 11))
        middle_cards = list(range(1, 11))
        p_1_score = p_2_score = 0

    def can_play(self,player,card):
        if player == 1:
            return card in self.p_1_cards
        return card in self.p_2_cards