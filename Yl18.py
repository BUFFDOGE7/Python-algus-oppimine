import random

def play_game():
    secret_number = random.randint(0, 100)
    attempts = 0

    print("Guess a number between 0 and 100.")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Correct! It took you {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

play_game()

while True:
    again = input("Play again? (yes/no): ").lower()
    if again == "yes" or again == "y":
        play_game()
    else:
        print("Goodbye!")
        break