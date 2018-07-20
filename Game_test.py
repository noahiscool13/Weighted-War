import unittest
from unittest import mock
from Game import *

class GameTest(unittest.TestCase):
    def test_init(self):
        test_ai_1 = mock.patch("Game.Player")
        test_ai_2 = mock.patch("Game.Player")
        game = Game(test_ai_1, test_ai_2)
        self.assertEqual(game.p1score, 0)


if __name__ == '__main__':
    unittest.main()
