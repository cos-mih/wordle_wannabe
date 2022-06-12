#!/bin/python3
from alphabet import alphabet
from dictionary import dictionary
import random
from termcolor import colored

class checked_letter:
    def __init__(self, letter):
        self.letter = letter
        self.color = "white"

    def set_to_green(self):
        self.color = "green"
    
    def set_to_yellow(self):
        self.color = "yellow"

    def set_to_white(self):
        self.color = "white"

class colored_alphabet:
    def __init__(self, alphabet):
        self.letters = alphabet.copy()
        for letter in self.letters:
            checked = checked_letter(letter)
            self.letters[self.letters.index(letter)] = checked

    def print(self):
        for letter in self.letters:
            print(colored(letter.letter, letter.color), end = " ")
            if self.letters.index(letter) in [9, 18, 25]:
                print("\n")

    def update(self, list):
        for letter in list:
            i = [let.letter for let in self.letters].index(letter.letter)
            if self.letters[i].color == "green" or self.letters[i].color == "grey":
                continue
            if letter.color == "white" and self.letters[i].color == "white":
                self.letters[i].color = "grey"
                continue
            if letter.color == "yellow" or letter.color == "green":
                self.letters[i].color = letter.color


def set_color(guess_letter, word_letters):
    temp_letters = word_letters.copy()

    for letter in guess_letter:
        checked = checked_letter(letter)

        if letter in temp_letters:
            if guess_letter.index(letter) == temp_letters.index(letter):
                checked.set_to_green()
                temp_letters[temp_letters.index(letter)] = " "
            else:
                checked.set_to_yellow()

        guess_letter[guess_letter.index(letter)] = checked

    for checked in guess_letter:
        if checked.color == "yellow":
            if checked.letter not in temp_letters:
                checked.set_to_white()
        if checked.color == "yellow":
            temp_letters[temp_letters.index(checked.letter)] = " "            


def get_valid_guess(dictionary):
    guess = input("Enter guess: ")

    while len(guess) != 5 or guess not in dictionary:
        guess = input("Try again with a valid word: ")

    return guess

def print_guess_board(guess_board):
    for i in range(6):
        print("| ", end = "")
        for j in range(5):
            print(colored(guess_board[i][j].letter, guess_board[i][j].color), end = "")
            print(" | ", end = "")
        print("\n")

def check_for_win(guess_letters):
    win = True
    for letter in guess_letters:
        if letter.color != "green":
            win = False
            break
    return win

def wordle():
    word = random.choice(dictionary).upper()
    alph = colored_alphabet(alphabet)

    word_letters = []
    for letter in word:
        word_letters.append(letter)

    guess_board = [[checked_letter(" ") for i in range(5)] for j in range(6)]

    for i in range(6):
        alph.print()
        guess = get_valid_guess(dictionary).upper()
        print("\n")

        guess_letters = list(guess)
        set_color(guess_letters, word_letters)

        alph.update(guess_letters)

        guess_board[i] = guess_letters
        print_guess_board(guess_board)
        win = check_for_win(guess_letters)
        if win:
            break

    if win:
        print("Yay, you got it! The word was: " + "".join(word_letters), end = "")
        print(" (%d/6)" %(i + 1))
    else:
        print("You lost :(\nThe word was: " + "".join(word_letters))
            

if __name__ == '__main__':
    wordle()
