"""
Load a dictionary file
Accept a name from user
Set limit = length of name
Start empty list to hold anagram phrase
While length of phrase < limit:
    Generate list of dictionary words that fit in name
    Present words to user
    Present remaining letters to user
    Present current phrase to user
    Ask user to input word or start over
If user input can be made from remaining letters:
    Accept choice of new word or words from user
    Remove letters in choice from letters in name
    Return choice and remaining letters in name
If choice is not a valid selection:
    Ask user for new choice or let user start over
Add choice to phrase and show to user
Generate new list of words and repeat process
When phrase length equals limit value:
Display final phrase
Ask user to start over or to exit
"""
from tools import load_dictionary
from collections import Counter

word_li = load_dictionary.load("2of12inf.txt")
words = set(word_li)
usr_input = input("Enter a word to search for anagrams: ").lower()

def anagram_phrase():
    anagram_li = []
    limit = len(usr_input)
    sort_usr_word = sorted(usr_input)
    usr_count = Counter(usr_input)
    while len(usr_input) < limit:
        for word in words:
            word = word.lower()
            if word != usr_input:
                if sort_usr_word == sorted(word):
                    anagram_li.append(word)
        return anagram_li

