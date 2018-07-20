

from Game import *
from AI_random import *

t = Tournament()

p1 = AI(t)
p2 = AI(t)

t.new_game(p1,p2)

t.play()