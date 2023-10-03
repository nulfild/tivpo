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
        pass
    def next_player(self):
        pass
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
