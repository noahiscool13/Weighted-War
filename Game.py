import random

class Game:



  p_1_cards = list(range(1, 11))
  p_2_cards = list(range(1, 11))
  middle_cards = list(range(1, 11))

  p1score = 0
  p2score = 0

  current = None

  def __init__(self,p1,p2):
    self.p1 = p1
    self.p2 = p2


  def newcard(self):
    self.current = random.choice(self.middle_cards)
    self.middle_cards.remove(self.current)

  def playcard(self,cardnum):
    pass

  def can_play(self,player,cardnum):
    if player == 1:
      return cardnum in self.p_1_cards
    return cardnum in self.p_2_cards


class Player:
    def __init__(self, tournament):
        self.tournament = tournament

    def current_game(self):
        return self.tournament.getCurrent()



