

def odd_and_even(list1: list [int]) -> list[int]:
    """Docstring"""
    i: int = 0
    list2: list[int] = []
    
    while i < len(list1):
        if list1[i] % 2 == 1 and i % 2 == 0:
            list2.append(list1[i])
        i += 1

    return list2












#def odd_and_even(numbers:list[int])-> list[int]:
    #numbers: list[int] = []
    #idx: int = 0
    #for element in numbers:
        #if element % 2 == 0.5 and idx(list) % 2 == 0.0:
            #numbers.append(element)
        #else:
            #None
    #return numbers 