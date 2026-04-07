"""
Load digital dictionary file as a list of words
Accept a word from user
Create an empty list to hold anagrams
Sort the user-word
Loop through each word in the word list:
Sort the word
if word sorted is equal to user-word sorted:
Append word to anagram list
Print anagram list
"""
from collections import Counter
from pprint import pprint

from tools import load_dictionary

dict_file = load_dictionary.load("2of12inf.txt")
dict_file = sorted(dict_file)
dict_file.append('a')
dict_file.append('i')
usr_word = input("Enter a word to find an anagram: ").lower()


def anagram_finder(name, word_li):
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_li:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print("Remaining letters = {}".format(name))
    print("Number of remaining letters = {}".format(len(name)))
    print("Number of remaining (real word) anagrams = {}".format(len(anagrams)))



