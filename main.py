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

    def kick_player(self, player_index):
        print("Покидает игру " + self.players[self.currentPlayerIndex])
        self.players.pop(self.currentPlayerIndex)
        if self.currentPlayerIndex == len(self.players):
            self.currentPlayerIndex = 0
    def get_random_word(self):
        pass
    def check_input(self, inputText):
        return bool(re.search(r'^[а-яА-Я]+$', inputText))
       
    def next_player(self):
        if self.currentPlayerIndex == len(self.players) - 1:
            self.currentPlayerIndex = 0
        else:
            self.currentPlayerIndex += 1
    def ask_for_input(self):
        input_text = input(self.players[self.currentPlayerIndex] +
                           ", введите букву или слово целиком: ")
        while not self.check_input(input_text) or input_text in self.used_letters:
            input_text = input(self.players[self.currentPlayerIndex] +
                               ", введите букву или слово целиком: ")
        return input_text.lower()
    def check_answer(self, guess):
        if len(guess) == 1:
            right_guess = False
            self.used_letters.add(guess)
            for ind in range(len(self.currentWord)):
                if self.currentWord[ind] == guess:
                    self.currentWordForAnswer = self.currentWordForAnswer[:ind] + guess + self.currentWordForAnswer[
                                                                                          ind + 1:]
                    right_guess = True
            if not right_guess: self.next_player()   
        else:
            if guess == self.currentWord:
                self.currentWordForAnswer = self.currentWord
            else:
                self.kick_player()
    def make_turn(self):
        pass
    def start(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.start()
