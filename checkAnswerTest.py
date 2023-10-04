import unittest
from main import Game

class TestCheckAnswerFunction(unittest.TestCase):

    def test_correct_single_letter_guess(self):
        game = Game()
        game.currentWord = "яблоко"
        game.currentWordForAnswer = "я****"
        game.check_answer("я")
        self.assertEqual(game.currentWordForAnswer, "я****")

    def test_incorrect_single_letter_guess(self):
        game = Game()
        game.currentWord = "яблоко"
        game.currentWordForAnswer = "*****"
        game.check_answer("н")
        self.assertNotEqual(game.currentWordForAnswer, "н****")
        
    def test_correct_full_word_guess(self):
        game = Game()
        game.currentWord = "банан"
        game.currentWordForAnswer = "*****"
        game.check_answer("банан")
        self.assertEqual(game.currentWordForAnswer, "банан")

    def test_incorrect_full_word_guess(self):
        game = Game()
        game.players = ["Player 1", "Player 2", "Player 3", "Player 4"]
        game.currentWord = "черри"
        game.currentWordForAnswer = "*****"
        game.check_answer("апельсин")
        self.assertNotEqual(game.currentWordForAnswer, "черри")
        self.assertEqual(len(game.players), 3)

    def test_letter_already_guessed(self):
        game = Game()
        game.currentWord = "охрана"
        game.currentWordForAnswer = "о*****"
        game.used_letters.add("о")
        game.check_answer("о")
        self.assertEqual(game.currentWordForAnswer, "о*****")
        self.assertEqual(game.currentPlayerIndex, 0)

    def test_next_player_called_on_incorrect_guess(self):
        game = Game()
        game.currentWord = "арбуз"
        game.currentWordForAnswer = "*****"
        initial_player_index = game.currentPlayerIndex
        game.check_answer("д")
        self.assertNotEqual(game.currentPlayerIndex, initial_player_index)

if __name__ == '__main__':
    unittest.main()
