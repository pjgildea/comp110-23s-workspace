def mimic(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
if letter_idx >= len(my_words):
    return ("Index to high")
#if we make it here, that means the letter_idx is valid
return my_words[letter_idx]