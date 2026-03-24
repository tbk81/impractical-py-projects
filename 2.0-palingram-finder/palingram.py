"""Find all word-pair palingrams in a dictionary file."""

from tools import load_dictionary

def find_palingrams(dict_txt):
    """Find dictionary palingrams."""
    word_li = load_dictionary.load(dict_txt)
    pali_li = []

    for word in word_li:
        if len(word) > 1:
            for l in word:
                print(l)


find_palingrams('2of12inf.txt')
