

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
  
def instructions ():
    print ("**** How To Play ****")
    print ()
    print ("The rules of the game go here")
    print ()
    return ""

# Main Routine goes here...

played_before = yes_no("Have you played this game before?")


if played_before == "no":
    instructions()

print("program continues")