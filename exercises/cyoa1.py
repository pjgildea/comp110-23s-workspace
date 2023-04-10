import random

points = 0
player = ""

def greet() -> None:
    """Prints a welcome message and asks for the player's name"""
    print("Welcome to the coinflip guessing game!")
    player = input("What is your name? ")

def coin_flip() -> str:
    """Returns the result of a coin flip"""
    result = random.choice(["Heads", "Tails"])
    print(f"The coin landed on {result}")
    return result

def guess() -> bool:
    """Asks the player to guess the coin flip and returns True if correct, False otherwise"""
    guess = input("Guess the coin flip (Heads or Tails): ")
    result = coin_flip()
    return guess == result

def play_game() -> None:
    """Plays a round of the coinflip guessing game"""
    global POINTS
    if guess():
        POINTS += 1
        print(f"Congratulations {PLAYER}! You guessed correctly.")
    else:
        print(f"Sorry {PLAYER}, you guessed incorrectly.")
        POINTS = 0

def main() -> None:
    """Entry point"""
    greet()
    while True:
        print(f"You have {POINTS} points.")
        print("1. Guess the coin flip")
        print("2. Quit")
        choice = input("What would you like to do? ")
        if choice == "1":
            play_game()
        elif choice == "2":
            print(f"Goodbye {PLAYER}! You accumulated {POINTS} points in the game.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



