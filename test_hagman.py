
import hangman
from wordlist import hanglist


def test_masked_word():
    assert hangman.masked_word("elephant",['e'])== 'e_e_____'
    
    