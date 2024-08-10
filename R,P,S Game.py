# ROCK,PAPER,SCISSORS GAME
import random
options = ("Rock", "Paper", "Scissors")
is_running = True

while is_running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter your choice (Rock,Paper,Scissors): ")
    print(f"player Choice: {player}")
    print(f"Computer Choice: {computer}")
        
    if player == computer:
            print("It's a Tie!")
    elif player == "Rock" and computer == "Scissors":
            print("You Won!")
    elif player == "Paper" and computer == "Rock":
            print("You Won!")
    elif player == "Scissors" and computer == "Paper":
            print("You Won!")
    else:
            print("You Lost!")

    if not input("Play Again? (y/n): ").lower() == 'y':
           is_running = False
print("Thanks For Playing!!!")
