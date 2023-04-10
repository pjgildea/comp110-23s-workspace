"""EX01 - Chardle - A cute step toward Wordle!"""
__author__ = "730465167"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character")
    exit()
count = 0
print("Searching for " + str(letter) + " in " + str(word))

if (word[0] == letter):
    print(letter + " found at index 0")
    count = count + 1
if (word[1] == letter):
    print(letter + " found at index 1")
    count = count + 1
if (word[2] == letter):
    print(letter + " found at index 2")
    count = count + 1
if (word[3] == letter):
    print(letter + " found at index 3")
    count = count + 1
if (word[4] == letter):
    print(letter + " found at index 4")
    count = count + 1

if count == 0:
    print("No instances of " + str(letter) + " found in " + str(word))

if count == 1:
    print(str(count) + " instance of " + str(letter) + " found in " + str(word))

if count >= 2:
    print(str(count) + " instances of " + str(letter) + " found in " + str(word))