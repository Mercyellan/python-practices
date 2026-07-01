import random

def play_guessing_game():
    # 1. Difficulty Levels
    difficulty = input("Choose difficulty - Easy, Medium, or Hard: ").strip().lower()

    if difficulty == "easy":
        lower_bound = 1
        upper_bound = 10
    elif difficulty == "medium":
        lower_bound = 1
        upper_bound = 100
    elif difficulty == "hard":
        lower_bound = 1
        upper_bound = 1000
    else:
        print("Invalid choice. Defaulting to Medium.")
        lower_bound = 1
        upper_bound = 100

    secret_number = random.randint(lower_bound, upper_bound)
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    # 2. Limited Guesses
    max_guesses = 7
    guess_count = 0
    guessed_correctly = False

    while guess_count < max_guesses and not guessed_correctly:
        try:
            guess = int(input(f"Take a guess ({max_guesses - guess_count} guesses left): "))
            guess_count += 1
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {guess_count} guesses!")
            guessed_correctly = True

    if not guessed_correctly:
        print(f"Sorry, you've run out of guesses! The number was {secret_number}.")


# 3. Play Again
play_again = "yes"
while play_again in ("yes", "y"):
    play_guessing_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()

print("Thanks for playing!")