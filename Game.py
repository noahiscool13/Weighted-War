import random

class Game:



  p_1_cards = list(range(1, 11))
  p_2_cards = list(range(1, 11))
  middle_cards = list(range(1, 11))

	p1score = 0
	p2score = 0

	current = None

  def __init__(self,p1:player,p2:player):
    self.p1 = p1
    self.p2 = p2


  def newcard(self):
    self.current = random.choice(middle_cards)
    self.middle_cards.remove(self.current)

  def playcard(self,cardnum:int)
    pass
  
  def can_play(self,player,card):
      if player == 1:
          return card in self.p_1_cards
      return card in self.p_2_cards

class player:
	def play(self):
		pass


