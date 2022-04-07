
show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error.

    show_instructions = input("have you played this game before?").lower()

    # If they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y" : 
        show_instructions = "yes" 
        print ("program continues")

    elif show_instructions == "no" or show_instructions == "n": 
        show_instructions = "no"
        print("display instructions")

    elif show_instructions == "ed sheeran": 
        print("i'm in love with the shape of you <3")

    else:
        print ("Please answer yes / no, and don't try to ed sheeran this <3")
    print ("You chose {}".format(show_instructions))

