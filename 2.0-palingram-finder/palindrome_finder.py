from tools import load_dictionary


word_li = load_dictionary.load('2of12inf.txt')
pal_li = []

for word in word_li:
    if len(word) > 1 and word == word[::-1]:
        pal_li.append(word)
print(f'There were {len(pal_li)} palindromes found out of {len(word_li)} words')
print(*pal_li, sep='\n')  # This will remove the quotes
