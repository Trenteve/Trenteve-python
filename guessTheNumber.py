import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print(f"Guess is too low. Try again.")
        elif guess > random_number:
            print(f"Guess is too high. Try again.")
    print(f"Yes {guess} was the right number!!")
guess(10)