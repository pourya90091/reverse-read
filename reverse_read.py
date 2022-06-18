from .data import equal_characters
from random import choice


def reverse_read(text: str, side=None):
    reversed_text = ""
    text = text.lower()

    tuples_data = []
    for key, value in equal_characters.items():
        tuple_data = (key, value)
        tuples_data.append(tuple_data)

    if side is None:
        side = []
        i = 0
        while i < 5:
            char = choice(text)

            for tuple_data in tuples_data:
                if char in tuple_data:
                    index = tuple_data.index(char)
                    if index == 0:
                        side.append(1)
                    else:
                        side.append(0)
            if len(side) == i:
                continue
            i += 1

        if side.count(0) > side.count(1):
            side = 0
        else:
            side = 1

    i = 0
    while i < len(text):
        for tuple_data in tuples_data:
            if text[i] in tuple_data:
                reversed_text += tuple_data[side]
                break
        if len(reversed_text) == i:
            reversed_text += text[i]
        i += 1

    return reversed_text
