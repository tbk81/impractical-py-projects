"""
The six most commonly used letters in the English language can be remembered
with the mnemonic “etaoin” (pronounced eh-tay-oh-in). Write a Python
script that takes a sentence (string) as input and returns a simple bar chart–
type display. Hint: I used a dictionary data structure and two
modules that I haven’t covered yet, pprint and collections/defaultdict.
"""
from collections import defaultdict

def main():
    sentence = "This is a sentence that needs a bar chart to display"
    li = list(sentence.lower().replace(' ', ''))
    li_dict = defaultdict(int)
    for k in li:
        li_dict[k] += 1

    for k, v in sorted(li_dict.items()):
        print(k, v*k)


if __name__ == "__main__":
    main()
