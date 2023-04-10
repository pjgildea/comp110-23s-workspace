def zip(key:list[str], value:list[int])-> dict [str,int]:
    if len(key) != len(value) or not key or not value:
        return {}
    else:
        result_dict = {}
        for i in range(len(key)):
            result_dict[key[i]] = value[i]
        return result_dict