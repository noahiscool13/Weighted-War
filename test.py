

from Game import *
from AI_random import AI as AI1
from AI_mirror import AI as AI2

t = Tournament()

p1 = AI1(t)
p2 = AI2(t)

t.new_game(p1,p2)

t.play()