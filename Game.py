import random

class Game:

  p_1_cards = list(range(1, 11))
  p_2_cards = list(range(1, 11))
  middle_cards = list(range(1, 11))

  p1score = 0
  p2score = 0

  current = None
  winner = None
  terminated = False
  
  def __init__(self,p1,p2):
    self.p1 = p1
    self.p2 = p2

  def turn(self,again=[]):
    current = random.choice(self.middle_cards)
    middle_cards.remove(current)

    try:
      self.newcard()
    except IndexError:
      return self.end_game()

    p1card = self.p1.play(current,1)
    p2card = self.p2.play(current,2)

    self.p_1_cards.remove(p1card)
    self.p_2_cards.remove(p2card)

    if self.can_play(1,p1card): 
      if self.can_play(2,p2card):
        if p1card > p2card:
          p1score += current + sum(again)
        elif p1card == p2card:
          return self.turn([current] + again)
        else:
          p2score += current + sum(again)
      else:
        self.p2score = -1
        self.end_game()
    else:
      self.p1score = -1
      self.end_game()

  def end_game(self):
    self.winner = 1 if self.p1score > self.p1score else 2
    self.winner = 0 if self.p1score == self.p2score else self.winner

    self.terminated = True

  def newcard(self):
    self.current = random.choice(self.middle_cards)
    self.middle_cards.remove(self.current)

  def can_play(self,player,cardnum):
    if player == 1:
      return cardnum in self.p_1_cards
    return cardnum in self.p_2_cards



class Player:
    def __init__(self, tournament):
        self.tournament = tournament

    def current_game(self):
        return self.tournament.getCurrent()




