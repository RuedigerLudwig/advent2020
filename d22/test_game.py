import unittest
from common.utils import read_file
from .factory import GameFactory


class TestXXX(unittest.TestCase):
    def setUp(self):
        lines = read_file("d22/data/sample1.txt")
        self.game = GameFactory.parse(lines)

    def test_parse_cards(self):
        expected = (5, 8, 4, 7, 10)
        result = self.game.p2.cards
        self.assertEqual(expected, result)

    def test_play_round_1(self):
        expected = (2, 6, 3, 1, 9, 5)
        round2 = self.game.single_round()
        result = round2.p1.cards
        self.assertEqual(expected, result)

    def test_play_round_2(self):
        expected = (8, 4, 7, 10)
        round2 = self.game.single_round()
        result = round2.p2.cards
        self.assertEqual(expected, result)

    def test_play_game(self):
        expected = (3, 2, 10, 6, 8, 5, 9, 4, 7, 1)
        last_round = self.game.play_game()
        result = last_round.p2.cards
        self.assertEqual(expected, result)

    def test_play_game_value(self):
        expected = 306
        last_round = self.game.play_game()
        result = last_round.p2.card_value
        self.assertEqual(expected, result)

    def test_play_advancedgame_value(self):
        expected = 291
        advanced = GameFactory.advanced(self.game)
        deck, _ = advanced.play_game()
        result = GameFactory.value(deck)
        self.assertEqual(expected, result)
