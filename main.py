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
        self.words = self.read_words('./words.csv')

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

    def kick_player(self):
        print("Покидает игру " + self.players[self.currentPlayerIndex])
        self.players.pop(self.currentPlayerIndex)
        if self.currentPlayerIndex == len(self.players):
            self.currentPlayerIndex = 0

    def get_random_word(self):
        return random.choice(self.words)

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
        input_text = self.ask_for_input()
        self.check_answer(input_text)

    def start(self):
        n = int(input("Введите количество игроков: "))
        while n < 1 or n > 5:
            print("Игроков должно быть от 1 до 5")
            n = int(input("Введите количество игроков: "))
        for i in range(n):
            self.players.append("Player " + str(i + 1))
        self.currentWord = self.get_random_word()
        self.currentWordForAnswer = "*" * len(self.currentWord)
        while self.currentWord != self.currentWordForAnswer and len(self.players) != 0:
            print("Текущее слово: " + self.currentWordForAnswer)
            self.make_turn()

        if len(self.players) == 0:
            print("К сожалению, никто не победил, слово было " + self.currentWord)
        else:
            print("И перед нами победитель..." + self.players[self.currentPlayerIndex])

if __name__ == "__main__":
    game = Game()
    game.start()
