import unittest
from main import Game

class TestReadWords(unittest.TestCase):
    def test_read_words_file1(self):
        game = Game()
        words = game.read_words("./words1.csv")
        true_words = ["вратарь", "фуникулер", "абсент", "воротник", "черепаха", "бергамот", "баклажан", "колибри", "хибара"]
        self.assertEqual(words, true_words)

    def test_read_words_file2(self):
        game = Game()
        words = game.read_words("./words2.csv")
        true_words = ["торонто", "кабачок", "структура", "улитка", "бассейн", "павлин", "манишка"]
        self.assertEqual(words, true_words)

    def test_read_words_file3(self):
        game = Game()
        words = game.read_words("./words3.csv")
        true_words = ["стремянка", "кувшин", "утконос", "испания", "валентин", "сосиска", "нагайка", "подорожник"]
        self.assertEqual(words, true_words)

    def test_read_words_default(self):
        game = Game()
        words = game.read_words("./words4.csv")
        true_words = ["вратарь", "черепаха", "бергамот", "баклажан", "колибри", "хибара"]
        self.assertEqual(words, true_words)

if __name__ == "__main__":
    unittest.main()