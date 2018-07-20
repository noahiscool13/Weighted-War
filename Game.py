import random

class Game:

  p_1_cards = list(range(1, 11))
  p_2_cards = list(range(1, 11))
  middle_cards = list(range(1, 11))

  p1score = p2score = 0

  winner = None
  terminated = False
  
  def __init__(self,p1,p2):
    self.p1 = p1
    self.p2 = p2

  def turn(self,again=[]):


    try:
      current = again + [random.choice(self.middle_cards)]
      self.middle_cards.remove(current[-1])
    except IndexError:
      return self.end_game()

    p1card = self.p1.move(current,1)
    p2card = self.p2.move(current,2)

    print("player 1 played card {}".format(p1card))
    print("player 2 played card {}".format(p2card))

    if self.can_play(1,p1card): 
      if self.can_play(2,p2card):
        self.p_1_cards.remove(p1card)
        self.p_2_cards.remove(p2card)
        if p1card > p2card:
          self.p1score += sum(current)
        elif p1card == p2card:
          return self.turn(current)
        else:
          self.p2score += sum(current)
      else:
        print("p2 made an illegal move. game terminated")
        self.p2score = -1
        self.end_game()
    else:
      print("p1 made an illegal move. game terminated")
      self.p1score = -1
      self.end_game()

  def end_game(self):
    self.winner = 1 if self.p1score > self.p1score else 2
    self.winner = 0 if self.p1score == self.p2score else self.winner

    self.terminated = True


  def can_play(self,player,cardnum):
    if player == 1:
      return cardnum in self.p_1_cards
    return cardnum in self.p_2_cards

class Player:
    def __init__(self, tournament):
        self.tournament = tournament

    def move(self, current, player):
      raise NotImplementedError

    def current_game(self):
        return self.tournament.current

class Tournament:
    game_list = []

    def new_game(self,p1,p2):
        self.game_list.append(Game(p1,p2))

    @property
    def current(self):
      return self.game_list[-1]

    def turn(self):
      self.current.turn()

    def play(self):
      while True:
        self.turn()
        print(self.current.p1score)
        print(self.current.p2score)
        if self.current.terminated:
          print(self.current.winner)
          return