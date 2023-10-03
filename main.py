import random
import csv
import re

class Game:
    currentWordForAnswer = ""
    currentWord = ""
    currentPlayerIndex = 0
    players = []
    used_letters = set()

    def __init__(self):
        pass
    def read_words(self, file_path):
        words = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                csvreader = csv.reader(file, delimiter='|')
                for row in csvreader:
                    words.append(row[0])
        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")
            print("Взяты слова по умолчанию")
            words = ["вратарь", "черепаха", "бергамот", "баклажан", "колибри", "хибара"]
        return words
    def next_player(self):
        if self.currentPlayerIndex == len(self.players) - 1:
            self.currentPlayerIndex = 0
        else:
            self.currentPlayerIndex += 1
    def kick_player(self, player_index):
        pass
    def get_random_word(self):
        pass
    def check_input(self, inputText):
        pass
    def ask_for_input(self):
        pass
    def check_answer(self, guess):
        pass
    def make_turn(self):
        pass
    def start(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.start()
