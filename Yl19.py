import random

def play_game():
    """Play one round of rock-paper-scissors"""
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    
    print("\nChoose: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()
    
    while user_choice not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        return 'win'
    else:
        print("Computer wins!")
        return 'loss'

def main():
    """Main game loop"""
    print("=== Rock-Paper-Scissors Game ===")
    
    wins = 0
    losses = 0
    ties = 0
    
    while True:
        result = play_game()
        
        if result == 'win':
            wins += 1
        elif result == 'loss':
            losses += 1
        else:
            ties += 1
        
        print(f"\nScore - Wins: {wins}, Losses: {losses}, Ties: {ties}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        while play_again not in ['yes', 'no', 'y', 'n']:
            play_again = input("Please enter 'yes' or 'no': ").lower()
        
        if play_again in ['no', 'n']:
            print("\nThanks for playing! Final score:")
            print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
            break

if __name__ == "__main__":
    main()