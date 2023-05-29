import random


def get_random_word(wordfile="/usr/share/dict/words"):
    candidate_words = []
    with open(wordfile) as f:
        for word in f:
            word = word.strip()
            if len(word) >= 6 and word.islower() and word.isalpha():
                candidate_words.append(word)
    word = random.choice(candidate_words)
    return word


def masked_word(word, tried_letters):
    guessed = ""
    for letter in word:
        if letter in tried_letters:
            guessed += letter
        else:
            guessed += "_"
    return guessed


def get_word(word):
    length = len(word) * "_"
    return length


def crct_guessed_letter(word, guess):
    guessed = ""
    for letter in word:
        if letter in guess:
            guessed += letter
        else:
            guessed += "_"
    return guessed
