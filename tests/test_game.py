import unittest
import string
from game import Game


class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_game_is_valid(self):
        new_game = Game()
        new_game.grid = list("BDAANDNEO")
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertIsInstance(new_game.is_valid(''), bool)
        self.assertIs(new_game.is_valid('ABANDONED'), True)

    def test_game_invalid(self):
        new_game = Game()
        new_game.grid = list("BDAANDNEO")
        self.assertIs(new_game.is_valid(''), False)
        self.assertIsNot(new_game.is_valid('ABANDON'), False)
