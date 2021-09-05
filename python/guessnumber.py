from random import randint

MAX_NUMBER = 100
number = randint(1, MAX_NUMBER)

guess = None
while guess != number:
    guess = input(f"Guess a number between 1 and {MAX_NUMBER}: ")

    try:
        guess = int(guess)
    except ValueError:
        print("That's not a number!")
        continue

    if guess > number:
        print("Too high try again.")
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Correct! Nice work!")
