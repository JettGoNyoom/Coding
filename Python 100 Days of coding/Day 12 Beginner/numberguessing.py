# Number guessing exercise
from random import randint
from art import logo

EASY_LVL_TURNS = 10
HARD_LVL_TURNS = 5

def chck_answ(guess, answer, turns):
    """checks answer against guess, returns num turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"Correct! The answer was {answer}!")

def set_diff():
    """sets the difficulty of the game"""
    level = input("Choose difficulty. Type 'easy' or 'hard'. If input does not match, will be automatically set to 'easy': ")
    if level.lower() == "hard":
        return HARD_LVL_TURNS
    else:
        return EASY_LVL_TURNS

def game():
    """the guessing game"""
    print(logo)
    # Choose random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    # Set number of turns
    turns = set_diff()

    # Pre-declaring guess
    guess = 0

    # Repeat guessing functionality if wrong
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number!")

        # User guessing the number
        guess = int(input("Make a guess: "))

        # Track # turns remaining, reduce by 1 if wrong
        turns = chck_answ(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose!")
            print(f"The answer was {answer}.")
            return
        elif guess != answer:
            print("Guess again.")

game()