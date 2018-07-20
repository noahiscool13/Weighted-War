

from Game import *
from AI_random import AI as AI1
from AI_mirror import AI as AI2

t = Tournament()

p1 = AI(t)
p2 = AI(t)

t.new_game(p1,p2)

t.play()