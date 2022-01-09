#!/usr/bin/python3
def common_elements(set_1, set_2):
    final =[]

    for i in set_1:
        for x in set_2:
            if i == x:
            final.append(i)

    return set(final)
