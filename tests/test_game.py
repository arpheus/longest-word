from unittest import TestCase
import string
from game import Game

class TestGame(TestCase):

    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_word_validation(self):
        game = Game()
        game.grid = ["A","B","N","D","E","F","G","U","I"]
        self.assertIs(game.is_valid("IGUANE"), True)
        self.assertIs(game.is_valid("BUFALO"), False)
        self.assertIs(game.is_valid(""), False)

    def test_unkown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list("KWIENFUQW")
        self.assertIs(new_game.is_valid("FEUN"), False)
