import unittest
from unittest.mock import patch
from io import StringIO
from main import Game

class TestGame(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["а", "Х", "а", "яблоко"])
    def test_valid_single_letter_input(self, mock_input, mock_stdout):
        game = Game()
        game.used_letters = set()
        game.players = ["Player1", "Player2"]
        game.currentPlayerIndex = 0
        result = game.ask_for_input()
        self.assertEqual(result, "а")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["123", "алыд2", "б"])
    def test_valid_word_input(self, mock_input, mock_stdout):
        game = Game()
        game.used_letters = set()
        game.players = ["Player1", "Player2"]
        game.currentPlayerIndex = 1
        result = game.ask_for_input()
        self.assertEqual(result, "б")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["", "о", "б"])
    def test_invalid_input_then_valid_input(self, mock_input, mock_stdout):
        game = Game()
        game.used_letters = set("о")
        game.players = ["Player1", "Player2"]
        game.currentPlayerIndex = 0
        result = game.ask_for_input()
        self.assertEqual(result, "б")

if __name__ == '__main__':
    unittest.main()
