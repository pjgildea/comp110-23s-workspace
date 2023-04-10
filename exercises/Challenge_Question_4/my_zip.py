
from my_zip import zip

def zip(key:list[str], value:list[int])-> dict [str, list]:
    result: dict [str, int] = ({})
    if key == list([]) and value == list ([]) or len(key) != len(value):
        return result