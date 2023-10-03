import unittest
from main import Game

class TestCheckAnswerFunction(unittest.TestCase):

    def test_correct_single_letter_guess(self):
        game = Game()
        game.currentWord = "apple"
        game.currentWordForAnswer = "*****"
        game.check_answer("a")
        self.assertEqual(game.currentWordForAnswer, "a****")

    def test_incorrect_single_letter_guess(self):
        game = Game()
        game.currentWord = "apple"
        game.currentWordForAnswer = "*****"
        game.check_answer("x")
        self.assertNotEqual(game.currentWordForAnswer, "x****")
        
    def test_correct_full_word_guess(self):
        game = Game()
        game.currentWord = "banana"
        game.currentWordForAnswer = "******"
        game.check_answer("banana")
        self.assertEqual(game.currentWordForAnswer, "banana")

    def test_incorrect_full_word_guess(self):
        game = Game()
        game.players = ["Player 1", "Player 2", "Player 3", "Player 4"]
        game.currentWord = "cherry"
        game.currentWordForAnswer = "******"
        game.check_answer("grape")
        self.assertNotEqual(game.currentWordForAnswer, "grape")

    def test_letter_already_guessed(self):
        game = Game()
        game.currentWord = "orange"
        game.currentWordForAnswer = "******"
        game.used_letters.add("o")
        game.check_answer("o")
        self.assertEqual(game.currentWordForAnswer, "o*****")
        self.assertEqual(game.currentPlayerIndex, 0)

    def test_next_player_called_on_incorrect_guess(self):
        game = Game()
        game.currentWord = "pear"
        game.currentWordForAnswer = "____"
        initial_player_index = game.currentPlayerIndex
        game.check_answer("x")
        self.assertNotEqual(game.currentPlayerIndex, initial_player_index)

if __name__ == '__main__':
    unittest.main()
