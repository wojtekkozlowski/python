import unittest
from other.tennis.tennis import *


class TennisTests(unittest.TestCase):

    def test_p1_scores_once(self):
        game = TennisGame('A', 'B')
        game.p1_score()
        self.assertEqual(game.get_score(), (15, 0))

    def test_p2_scores_once(self):
        game = TennisGame('A', 'B')
        game.p2_score()
        self.assertEqual(game.get_score(), (0, 15))

    def test_p1_p2_score(self):
        game = TennisGame('A', 'B')
        game.p1_score()
        game.p2_score()
        self.assertEqual(game.get_score(), (15, 15))

    def test_p1_scores_twice(self):
        game = TennisGame('A', 'B')
        game.p1_score()
        game.p1_score()
        self.assertEqual(game.get_score(), (30, 0))

    def test_p1_scores_thrice(self):
        game = TennisGame('A', 'B')
        game.p1_score()
        game.p1_score()
        game.p1_score()
        self.assertEqual(game.get_score(), (40, 0))

    def test_p1_wins(self):
        game = TennisGame('A', 'B')
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p1_score()
        self.assertEqual(game.get_score(), (0, 0))
        self.assertEqual(game.get_games_won(), (1, 0))

    def test_p1_wins_and_scores_30(self):
        game = TennisGame('A', 'B')
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p2_score()
        game.p2_score()
        self.assertEqual(game.get_score(), (30, 30))
        self.assertEqual(game.get_games_won(), (1, 0))

    def test_deuce(self):
        game = TennisGame('A', 'B')
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p2_score()
        game.p2_score()
        game.p2_score()
        self.assertEqual(game.get_score(), (40, 40))

    def test_p1_gets_adv(self):
        game = TennisGame('A', 'B')
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p2_score()
        game.p2_score()
        game.p2_score()
        game.p1_score()
        self.assertEqual(game.get_score(), (45, 40))

    def test_p2_gets_adv(self):
        game = TennisGame('A', 'B')
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p2_score()
        game.p2_score()
        game.p2_score()
        game.p2_score()
        self.assertEqual(game.get_score(), (40, 45))

    def test_p2_loses_adv(self):
        game = TennisGame('A', 'B')
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p2_score()
        game.p2_score()
        game.p2_score()
        game.p2_score()
        game.p1_score()
        self.assertEqual(game.get_score(), (40, 40))

    def test_p1_loses_adv(self):
        game = TennisGame('A', 'B')
        game.p2_score()
        game.p2_score()
        game.p2_score()
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p2_score()
        self.assertEqual(game.get_score(), (40, 40))

    def test_p2_loses_gains_adv_and_wins(self):
        game = TennisGame('A', 'B')
        game.p2_score()
        game.p2_score()
        game.p2_score()
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p1_score()
        game.p2_score()
        game.p2_score()
        game.p2_score()
        game.p2_score()
        self.assertEqual(game.get_score(), (0, 15))
        self.assertEqual(game.get_games_won(), (0, 1))
