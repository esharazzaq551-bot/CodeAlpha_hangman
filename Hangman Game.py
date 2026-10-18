# Hangman Game
# CodeAlpha Python Programming Internship - Task 1
# Author: Esha Razzaq

import random

# List of 5 predefined words
WORDS = ["python", "coding", "laptop", "keyboard", "program","Codealpha"]

# Maximum number of wrong guesses allowed
MAX_WRONG = 6


def show_word(secret_word, guessed_letters):
    """Return the word with unguessed letters hidden as underscores."""
    display = ""

    # Go through each letter of the secret word
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter + " "   # show the guessed letter
        else:
            display = display + "_ "           # hide the unknown letter

    return display


# Choose a random word from the list
secret_word = random.choice(WORDS)

# Keep track of the game
guessed_letters = []   # all letters the player has guessed
wrong_guesses = 0      # number of wrong guesses so far

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You can make only", MAX_WRONG, "wrong guesses.")

# Keep playing until the player runs out of wrong guesses
while wrong_guesses < MAX_WRONG:
    current_word = show_word(secret_word, guessed_letters)

    # Show the current status of the game
    print()
    print("Word:", current_word)
    print("Wrong guesses left:", MAX_WRONG - wrong_guesses)
    print("Guessed letters:", guessed_letters)

    # If there are no underscores left, the player has won
    if "_" not in current_word:
        print("Congratulations! You won!")
        break

    # Take the guess from the player
    guess = input("Guess a letter: ").lower().strip()

    # Check the guess and respond
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            wrong_guesses = wrong_guesses + 1
            print("Wrong guess!")

# If the loop ended because the player used all guesses, the game is lost
if wrong_guesses == MAX_WRONG:
    print()
    print("Game over! The word was:", secret_word)