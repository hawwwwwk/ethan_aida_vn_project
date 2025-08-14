# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("character1") # character #1
define b = Character("character2") # character #2
define c = Character("character3") # character #3
define yn = Character("[ynName]") # y/n

# default heshe="he"
# default himher="him"
# default hishers="his"
# default ynName = "Aida"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    menu gender_choice:
        "Prefered pronouns?"
        "He/him":
            $ gender = "m"
        "She/her":
            $ gender = "f"
        "They/them":
            $ gender = "t"

    if gender == "m":
        $ heshe = "he" 
        $ himher = "him"
        $ hisher = "his"
    elif gender == "f":
        $ heshe = "she"
        $ himher = "her"
        $ hisher = "her"
    else: # gender = t
        $ heshe = "they"
        $ hisher = "their"
        $ hisher = "their"
        
    $ ynName = renpy.input("What's your name?", "", length=16, exclude=" 0123456789+=,.?!<>{}[]()").strip() or "y/n"

    scene bg room

    # These display lines of dialogue.

    yn "You've created a new Ren'Py game."

    # This ends the game.

    return
