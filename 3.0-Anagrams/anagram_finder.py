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
from tools import load_dictionary

word_li = load_dictionary.load("2of12inf.txt")
words = set(word_li)

def anagram_finder():
    anagram_li = []
    usr_word = input("Enter a word to find an anagram: ").lower()
    sort_usr_word = sorted(usr_word)
    for word in words:
        word = word.lower()
        if word != usr_word:
            if sort_usr_word == sorted(word):
                anagram_li.append(word)
    return anagram_li


print(anagram_finder())
