"""EX03 Structured Wordle"""
__author__ = "730465167"

def contains_char(word: str, character: str)-> bool:
    """Returns True if a character is found in any index in the word, false if otherwise"""
    assert len(character) == 1 
    num: int  = 0
    while (num < len(word)):
        if word[num] == character:
            return True
        num = num + 1
    return False

    #if word[0] == character:
    #    return True
    #if word[1] == character:
    #    return True
    #if word[2] == character:
    #    return True
    #if word[3] == character:
    #    return True
    #if word[4] == character:
    #    return True
    #else:
    #    return False
    #
quit()