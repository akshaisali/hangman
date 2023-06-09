import hangman
import os
import tempfile


def test_select_random_word_min_length():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["cat\n", "elephant\n", "mouse\n", "dog\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "elephant"

    os.unlink(name)


def test_select_random_word_no_non_alpha_chars():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["pine's\n", "Dr.\n", "Ångström\n", "policeman\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "policeman"

    os.unlink(name)


def test_select_random_word_no_capitals():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["Alexander\n", "AMD\n", "California\n", "pelican\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "pelican"

    os.unlink(name)


def test_select_random_word_no_repetitions():
    secret_words = set()
    for _ in range(10):
        secret_words.add(hangman.get_random_word())
    assert len(secret_words) == 10


def test_masked_word():
    assert hangman.masked_word("elephant", ["e"]) == "e_e_____"


def test_get_word():
    secret_value = hangman.get_word("elephant")
    assert secret_value == "________"


def test_crct_guessed_letter():
    assert hangman.crct_guessed_letter("elephant", ["p"]) == "___p____"


def test_wrong_guessed_letter():
    assert hangman.crct_guessed_letter("elephant", ["x"]) == "________"


def test_no_guessed_letter():
    assert hangman.crct_guessed_letter("elephant", [" "]) == "________"


def test_rep_guessed_letter():
    assert hangman.crct_guessed_letter("elephant", ["e"]) == "e_e_____"
