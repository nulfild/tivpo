import unittest

from main import Game


class TestCheckInput(unittest.TestCase):

    def test_correct_input_one_letter(self):
        game = Game()
        self.assertEqual(game.check_input("а"), True)

    def test_correct_input_word(self):
        game = Game()
        self.assertEqual(game.check_input("арбуз"), True)


    def test_incorrect_input_letter(self):
        game = Game()
        self.assertEqual(game.check_input("d"), False)

    def test_incorrect_input_word(self):
        game = Game()
        self.assertEqual(game.check_input("ДРУJBA"), False)

    def test_incorrect_input_word_with_special_symbols(self):
        game = Game()
        self.assertEqual(game.check_input(" кот "), False)

if __name__ == "__main__":
    unittest.main()
