import unittest

from main import Game


class TestKickPlayer(unittest.TestCase):

    def test_kick_player_not_last(self):
        game = Game()
        game.players = ["Player 1", "Player 2", "Player 3", "Player 4"]
        game.currentPlayerIndex = 2
        game.kick_player()
        self.assertEqual(game.currentPlayerIndex, 2)
        self.assertEqual(len(game.players), 3)

    def test_kick_player_last(self):
        game = Game()
        game.players = ["Player 1", "Player 2", "Player 3", "Player 4"]
        game.currentPlayerIndex = 2
        game.kick_player()
        game.kick_player()
        self.assertEqual(game.currentPlayerIndex, 0)
        self.assertEqual(len(game.players), 2)


if __name__ == "__main__":
    unittest.main()
