

from Game import *
from AI_random import AI as AI1
from AI_mirror import AI as AI2


p1 = AI1()
p2 = AI2()

t = Tournament(p1,p2)



print(t.playngames(100))
