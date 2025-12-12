import random

def play_game():
    secret_number = random.randint(0, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 100.")
    print("Try to guess it!\n")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"\nCongratulations! You guessed it right!")
                print(f"The number was {secret_number}")
                print(f"It took you {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.\n")
            else:
                print("Too high! Try a lower number.\n")
                
        except ValueError:
            print("Please enter a valid number.\n")

if __name__ == "__main__":
    play_game()
    
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again == "yes" or play_again == "y":
            print("\n" + "="*40 + "\n")
            play_game()
        else:
            print("Goodbye!")
            break