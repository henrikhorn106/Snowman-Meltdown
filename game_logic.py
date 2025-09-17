import random

from ascii_art import STAGES
from words import WORDS


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current game state."""

    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("Guessed Letters: ", ", ".join(guessed_letters))
    print("Attempts left: ", len(STAGES) - mistakes)


def play_game():
    print("Welcome to Snowman Meltdown!")

    play_again = True
    while play_again:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        round_number = 1

        # Enter the game loop.
        while True:

            if all(letter in guessed_letters for letter in secret_word):
                print("\nCongratulations, you saved the snowman!")
                break

            if mistakes == len(STAGES):
                print(f"\nGame Over! The word was: {secret_word}")
                break

            print(f"\n=====[Round {round_number}]=====")
            # Display the initial game state.
            display_game_state(mistakes, secret_word, guessed_letters)

            while True:
                # Prompt user for one guess.
                guess = input("\nGuess a letter: ").strip().lower()

                if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
                    break

                if len(guess) != 1:
                    print("Invalid input. Please enter a single letter.")

                if guess in guessed_letters:
                    print(f"You already guessed the letter {guess}.")

            if guess in secret_word:
                print(f"Good guess! {guess} is in the word.")
                guessed_letters.append(guess)

            else:
                print(f"Sorry, {guess} is not in the word.")
                mistakes += 1

            round_number += 1

        # Enter the Replay loop.
        while True:
            option = input("\nDo you want to play again? (y/n) ").strip().lower()

            if option.lower() == "n":
                play_again = False
                break
            elif option.lower() == "y":
                play_again = True
                break
            else:
                print("Invalid input. Please enter y or n.")


if __name__ == "__main__":
    play_game()
