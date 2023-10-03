import unittest
from main import Game

class TestNextPlayer(unittest.TestCase):
    def test_next_player_inex_med(self):
        game = Game()
        game.players = ["Player 1", "Player 2", "Player 3"]
        game.currentPlayerIndex = 1

        game.next_player()

        self.assertEqual(game.currentPlayerIndex, 2)

    def test_next_player_inex_end(self):
        game = Game()
        game.players = ["Player 1", "Player 2", "Player 3"]
        game.currentPlayerIndex = 2

        game.next_player()

        self.assertEqual(game.currentPlayerIndex, 0)

if __name__ == "__main__":
    unittest.main()