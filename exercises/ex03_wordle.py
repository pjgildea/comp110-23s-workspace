"""EX03 Structured Wordle"""
__author__ = "730465167"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    #variables 
    secret: str = "codes"
    number_of_turns: int = 0
    max_turns: int = 6
    winner: bool = False
    #while loop
    while(number_of_turns < max_turns) and not winner: #means max # of turns is 5, starting at 0, so number of times can go up to that
        number_of_turns += 1 #number of turns +1
        print(f"=== Turn {number_of_turns}/{max_turns} ===") #use of fstring 
        guess = input_guess(len(secret)) #checking to see if the length of the secret is equal to the length of the input guess
        result = emojified(guess,secret) #if the above line is true, next step is turning guess into green,yellow,white boxes
        if guess == secret: #if the guess is the same value as the secret "codes", you move on
            winner = True #boolean statement, winner is changed from false to true
            print(result)
        else:
            print(result)
    if winner:
        print(f"You won in {number_of_turns}/{max_turns} turns!") #if you win, determined by True = winner, this f string message appears
    else:
        print(f"X/{max_turns}  - Sorry, try again tomorrow!") #if you lose, determind by False = winner, this f string appears

def contains_char(word: str, character: str)->bool: #first function defined, contains char
    """Returns True if a character is found in any index in the word, false if otherwise"""
    assert len(character) == 1 
    idx: int  = 0
    while (idx < len(word)): #while the number is less than the length of the word, move on into the if statement.
        if word[idx] == character: #if the in
            return True
        idx = idx + 1
    return False

def emojified(guess: str, secret: str)->str:
    """Returns green box if letter is in correct spot, yellow box just if correct letter is guessed, white box is letter is incorrect"""
    assert len(guess) == len(secret)
    result: str = "" #result begins with nothing, this helps us concatenate later on
    idx: int = 0
    while(idx < len(guess)):
        if(contains_char(secret,guess[idx])):
            #print green or yellow
            if (guess[idx] == secret[idx]): #will check if first letter of guess equals first letter of secret
                result = result + "\U0001F7E9" #result is "" + green box (concatenate)
            else:
                result = result + "\U0001F7E8" #result is "" + yellow box (concatenate)
        else:
            result = result + "\U00002B1C" #result is "" + white box (concatenate)
        idx = idx + 1 #this allows you to move to the next index
    return(result) #returns your emojies you concatenate once index is the same as the length of guess

def input_guess(expected_length:int)->str:
    """Returns error message to user if their guessed word is not equal to the expected length"""
    guess = input(f"Enter a {expected_length} character word:") #f string that checks that the input is equal to the expected length
    while (len(guess)!= expected_length): #if the input is not equal to the expected length go to the next line
        guess = input(f"That wasn't {expected_length} chars! Try again: ") #sends a message to the user letting them know it does not work, goes back to top of while statement
    return(guess) #once the expected length equals the user input, it will return the guess made by the user


if __name__ == "__main__":
    main()
