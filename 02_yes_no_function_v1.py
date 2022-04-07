

# Functions go here...
from tkinter import Y


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()


        if response == "yes" or response == "y" : 
            # response = "yes" 
            return "yes"

        elif response == "no" or response == "n": 
            # response = "no"
            return "no"

        elif response == "ed sheeran": 
            print("i'm in love with the shape of you <3")
            return "ed sheeran"
        
        else:
            print ("Please answer yes / no, and don't try to ed sheeran this <3")
  

# Main Routine goes here...

show_instructions = yes_no("Have you played this game before?")
print("You chose {}".format(show_instructions))

if show_instructions == "yes":
    print("game continues")
else:
    print("display instructions")

print()
having_fun = yes_no("Are you having fun?")
print("You said {} to having fun".format(having_fun))

print()
ed_sheeran = yes_no("Do you like Ed Sheeran?")
print("You said {} to liking Ed Sheeran. Fun fact, he was born on the 17th February, 1991. \OwO/ ".format(ed_sheeran))
