#! /usr/bin/env python3
# coding: utf-8
from random import choice

def hangman():
    words_list = ["python", "java", "kotlin", "javascript"]
    word_to_guess = choice(words_list)
    word_displayed = '-' * len(word_to_guess)
    tries_allowed = 8
    mistakes = 0
    computer_guesses = []

    print("H A N G M A N")

    while mistakes < tries_allowed:
        print()
        print(word_displayed)
        if word_displayed == word_to_guess:
                print(word_to_guess)
                print("You guessed the word!")
                print("You survived!")
                return
        computer_guess = input(f"Input a letter: ")
        if len(computer_guess) > 1:
            print("You should input a single letter")
        elif not (123 > ord(computer_guess) > 96):
            print("It is not an ASCII lowercase letter")
        elif computer_guess in computer_guesses:
            print("You already typed this letter")
        elif computer_guess in word_to_guess:
            word_displayed = list(word_displayed)
            for index, letter in enumerate(word_to_guess):
                if letter == computer_guess:
                    word_displayed[index] = letter
            word_displayed = "".join(word_displayed)
        else:
            print("No such letter in the word")
            mistakes += 1
        computer_guesses.append(computer_guess)

    print("You are hanged!")
    return

def play_or_exit(status = None):
    while status != "play":
        status = input("Type \"play\" to play the game, \"exit\" to quit: ")
        if status == "exit":
            exit()
    return True

def main():
    while play_or_exit():
        hangman()

if __name__ == "__main__":
    main()
