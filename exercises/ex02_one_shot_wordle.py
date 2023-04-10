"""One Shot Wordle--Loops!"""
__author__ = "730465167"

SECRET = "python"
guess = ""

while (len(guess) != 6):
    guess: str = input("What is your 6-letter guess? ")
    if guess == SECRET:
        print("Woo! You got it! ")
else: 
        print("Not exactly! ")    
        if (len(guess) != 6): 
            print ("That wasn't six-letters! ")
            guess: str = input("That was not 6 letters! Try again: ") 
        else: #guess has 6 letters
            print("Not quite! Play again soon! ")
     
     
     
     
     
     
     
        #if  ##check each letter of the guess compared to secret word
            ## if letter correct and in right spot its green
            # if letter correct and in wrong spot its yellow
            # if letter incorrect and wrong spot its white 
#spot : bool = False
#correct_letter : bool = False