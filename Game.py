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
        self.p2score = -1
        self.end_game()
    else:
      self.p1score = -1
      self.end_game()

  def end_game(self):
    self.winner = 1 if self.p1score > self.p2score else 2
    self.winner = 0 if self.p1score == self.p2score else self.winner

    self.terminated = True


  def can_play(self,player,cardnum):
    if player == 1:
      return cardnum in self.p_1_cards
    return cardnum in self.p_2_cards

class Player:
    def register_tournament(self,tournament):
        self.tournament = tournament

    def move(self, current, player):
      raise NotImplementedError

    def current_game(self):
        return self.tournament.current_game()

class Tournament:
    game_list = []

    def __init__(self,p1,p2):
      self.p1 = p1
      self.p2 = p2

      p1.register_tournament(self)
      p2.register_tournament(self)

    def new_game(self):
       self.game_list.append(Game(self.p1,self.p2))

    def current_game(self):
      return self.game_list[-1]

    def turn(self):
      self.current_game().turn()

    def playngames(self,n):
      winnerlist = []

      for i in range(n):
        self.new_game()
        g = self.play()
        print(self.game_list)
        winner = g.winner
        p1score = g.p1score 
        p2score = g.p2score 
        winnerlist.append(winner)

      print(winnerlist)

      return max(set(winnerlist), key=winnerlist.count)

    def play(self):
      while True:
        if self.current_game().terminated:
          return self.current_game()
        self.turn()

