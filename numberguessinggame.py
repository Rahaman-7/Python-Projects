# PYTHON NUMBER GUESSING GAME
import random

low = 1
high = 100
guesses = 0
answer = random.randint(low, high)
is_running = True
print("WELCOME TO PYTHON NUMBER GUESSING GAME")
print(f"enter the number between ({low}-{high}): ")

while is_running:
    guess = input("Enter your Guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess<low or guess>high:
            print("That Number is Out of range")
            print(f"Please Enter the number between ({low}-{high}): ")
        elif guess<answer:
            print("Too Low!, Try Again!")
        elif guess>answer:
            print("Too High!, Try Again!")
        else:
            print(f"CORRECT!, The Answer was {answer}")
            print(f"Number of Guesses: {guesses}")
            is_running = False
    else:
        print("Invalid Guess!")
        print(f"Please Enter the number between ({low}-{high}): ")






