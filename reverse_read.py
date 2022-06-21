from .data import equal_characters
from random import choice
from re import findall


tuples_data = []
for key, value in equal_characters.items():
    tuple_data = (key, value)
    tuples_data.append(tuple_data)


def reverse_read(text: str, side=None, sensible=False):
    reversed_text = ""
    text = text.lower()

    if side is None:
        side = set_side(text)

    i = 0
    while i < len(text):
        for tuple_data in tuples_data:
            if text[i] in tuple_data:
                reversed_text += tuple_data[side]
                break
        if len(reversed_text) == i:
            reversed_text += text[i]
        i += 1

    if sensible is True:
        if side == 0:
            language = "english"
        else:
            language = "persian"

        sensible = sense_scan(reversed_text, language)
        if not sensible:
            return -1

    return reversed_text


def set_side(text: str):
    side = 0
    i = 0
    while i < 5:
        char = choice(text)
        for tuple_data in tuples_data:
            if char in tuple_data:
                index = tuple_data.index(char)
                if index == 0:
                    side += 1
            else:
                continue
        i += 1

    if side <= 2:
        side = 0
    else:
        side = 1

    return side


def sense_scan(text: str, language: str):
    with open(f'./words/{language}_words.txt', 'r', encoding='utf-8') as word_file:
        relevant_words = set(word_file.read().split())

    words = findall(r"[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z]+[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z-_]*", text)

    score = 0
    i = 0
    while i < 5:
        word = choice(words)
        if word in relevant_words:
            score += 1
        i += 1
    
    if score > 2:
        return True
    else:
        return False
