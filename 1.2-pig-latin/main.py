"""
Pig latin module
"""
def pig_func(usr_input):
    """
    This takes input from the user and converts the string into pig latin
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    eng_li = usr_input.lower().split()
    pig_li = []
    for word in eng_li:
        if word[0] in vowels:
            pig_li.append([word[1:]+word[0]+"hay"])
        else:
            pig_li.append(word[1:]+word[0]+"ay")
    return ' '.join(pig_li)

def main():
    """
    The main function that asks the user for input and prints the output of the pig_func
    """
    pig_latin = pig_func(input("Enter a word or phrase to conver to Pig Latin: "))
    print(pig_latin)


if __name__ == "__main__":
    main()
