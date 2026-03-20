"""
Load a list of first names
Load a list of surnames
Choose a first name at random
Assign the name to a variable
Choose a surname at random
Assign the name to a variable
Print the names to the screen in order and in red font
Ask the user to quit or play again
If user plays again:
repeat
If user quits:
end and exit
"""

from random import choice
def main():
    """
    Create a silly name with this name generator
    """
    first_li = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'", "Bob 'Stinkbug'", 'Bowel Noises',
                'Boxelder', "Bud 'Lite'", 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy',
                'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
                'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim',
                'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass',
                'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks',
                'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy',
                'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
                'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea', 'TeeTee',
                'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms')

    last_li = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof',
               'Clutterbuck', 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith', 'Goodpasture',
               'Guster', 'Henderson', 'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt',
               'Johnson', 'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy',
               'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson',
               'Pieplow', 'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
               'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
               'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey',
               'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')

    run = True
    print("Welcome to the Silly Name Generator!")
    while run:
        usr_response = input("Generate a Silly Name? (yes/no)").lower()
        if usr_response in ("yes", "y"):
            first_name = choice(first_li)
            last_name = choice(last_li)
            silly_name = first_name + " " + last_name
            print(f"\033[31m{silly_name}\033[0m")
        elif usr_response in ("no", "n"):
            print("Thanks for playing!")
            run = False
        else:
            print("\033[36mPlease type yes or no\033[0m")


if __name__ == "__main__":
    main()
