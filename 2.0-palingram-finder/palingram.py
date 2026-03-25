"""Find all word-pair palingrams in a dictionary file."""

from tools import load_dictionary

word_li = load_dictionary.load('2of12inf.txt')
def find_palingrams():
    """Find dictionary palingrams."""
    pali_li = []

    for word in word_li:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for l in range(end):
                if word[l:] == rev_word[:end - l] and rev_word[end - l:] in word_li:
                    pali_li.append((word, rev_word[end - l:]))
                if word[:l] == rev_word[end - l:] and rev_word[:end - l] in word_li:
                    pali_li.append((rev_word[:end - l], word))
    return pali_li


palingrams = find_palingrams()
print(f'There were {len(palingrams)} palindromes found')
print(*palingrams, sep='\n')
