import random

options = ['rock', 'paper', 'scissors']
wins = losses = ties = 0

while True:
    computer = random.choice(options)
    user = input("rock, paper, or scissors: ").lower()

    while user not in options:
        user = input("Invalid. Try again: ").lower()

    print(f"Computer chose: {computer}")

    if user == computer:
        print("Tie!")
        ties += 1
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("You win!")
        wins += 1
    else:
        print("Computer wins!")
        losses += 1

    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")

    again = input("Play again? (yes/no): ").lower()
    if again in ['no', 'n']:
        break