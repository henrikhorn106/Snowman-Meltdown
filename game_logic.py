import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
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


def play_game():


    print("Welcome to Snowman Meltdown!")

    play_again = True
    while play_again:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        round = 1

        while True:

            if len(guessed_letters) == len(set(secret_word)):
                print("\nCongratulations, you saved the snowman!")
                break

            if mistakes == 8:
                print(f"\nGame Over! The word was: {secret_word}")
                break


            print(f"\n=====[Round {round}]=====")
            # Display the initial game state.
            display_game_state(mistakes, secret_word, guessed_letters)

            while True:
                # Prompt user for one guess
                guess = input("\nGuess a letter: ").lower()

                if len(guess) == 1 and guess.isalpha():
                    print("You guessed:", guess)
                    break

                print("Invalid input. Please enter a single letter.")

            if guess in secret_word:
                guessed_letters.append(guess)

            else:
                mistakes += 1

            round += 1


        while True:
            option = input("\nDo you want to play again? (y/n) ")

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
