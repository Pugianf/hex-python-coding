#!/usr/bin/python3
def best_score(a_dictionary):
    numbers = []
    try:
        for key in a_dictionary:
            if isinstance(a_dictionary[key], int):
                numbers.append(a_dictionary.get(key))
        return list(a_dictionary.keys())[numbers.index(max(numbers))]

    except:
        return None
