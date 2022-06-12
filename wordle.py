#!/bin/python3
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

def set_color(guess_letter, word_letters):
    for letter in guess_letter:
        checked = checked_letter(letter)

        if letter in word_letters:
            if guess_letter.index(letter) == word_letters.index(letter):
                checked.set_to_green()
            else:
                checked.set_to_yellow()

        guess_letter[guess_letter.index(letter)] = checked

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

    word_letters = []
    for letter in word:
        word_letters.append(letter)

    guess_board = [[checked_letter(" ") for i in range(5)] for j in range(6)]

    for i in range(6):
        guess = get_valid_guess(dictionary).upper()

        guess_letters = list(guess)
        set_color(guess_letters, word_letters)

        guess_board[i] = guess_letters
        print_guess_board(guess_board)
        win = check_for_win(guess_letters)
        if win:
            break

    if win:
        print("Yay, you got it! The word was: " + "".join(word_letters))
    else:
        print("You lost :(\nThe word was: " + "".join(word_letters))
            

if __name__ == '__main__':
    wordle()
