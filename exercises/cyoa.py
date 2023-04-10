"""Create your own adventure."""
__author__ = "730465167"

import random

POINTS_TO_WIN = 5

points: int = 0
player: str = ""
record: int = 0


def greet() -> None:
    """Message to give context to game and asks the player for their name."""
    print("Welcome to coin flip! Guess 5 in a row correctly to win!")
    global player  
    player = input("What is your name? ")
    print(f"Hello {player}!")


def coin_flip() -> str:
    """Returns the result of a coin flip."""
    result = random.choice(['heads', 'tails'])
    print(f"The coin landed on {result}")
    return result

   
def guess() -> bool:
    """Returns True or False if user guesses correctly."""
    guess = input("Awesome! Guess the coin flip: heads or tails (casesensitive!) ")
    result = coin_flip()
    return guess == result
      
      
def playgame(points: int) -> int:
    """Plays a round of the coinflip game, and updates personal record if applicable."""
    global record
    if guess():
        points += 1
        print(f"Congratulations {player}! You guessed correctly.")
        if points > record:
            record = points
            if record >= POINTS_TO_WIN:
                print(f"You Win! You have {record} in a row! ")
            else:
                print("You are getting closer to winning! ")    
    else:
        print(f"Sorry {player}, you guessed incorrectly.")
        points = 0
    return points
       

def main() -> None:
    """Entry point."""
    global points
    global player
    global record
    greet()
    while True:
        if points == 0:
            print(f"You currently have {points} points. Are you ready to make some?")
        else:
            print(f"You are on a {points} point streak! Dare to make more?")
        print("Press 1 if you with to guess the coin flip. ")
        print("Press 2 if you wish to exit. ")
        choice = input("")
        if choice == "1":
            points = playgame(points)
        elif choice == "2":
            print(f"Goodbye {player}! You finish with {points} points!")
            quit()
        else:
            print("Invalid choice. Please type a 1 or a 2. ")


if __name__ == "__main__":
    main()







