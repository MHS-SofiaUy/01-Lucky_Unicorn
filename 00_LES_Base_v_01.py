import random

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
            print ("Please answer yes / no")


def instructions ():
    print ("**** How To Play 101 ****")
    print ()
    print ("You can choose a starting amount to play with. (From $1 - $10)")
    print()
    print("Every round will cost $1, and depending on your prize, you may earn some money back, or get some money taken away")
    print()
    print("Then, press <enter> to play. You will either get a Horse, a Zebra, a Donkey or the best prize, Ed Sheeran!")
    print()
    print("Here are the tokens and their value:")
    print("Ed Sheeran: $5:00 (You earn back $4:00)")
    print("Horse: $0.50 (You lose $0.50)")
    print("Zebra: $0.50 (You lose $0.50)")
    print("Donkey: $0.00 (You lose $1.00)")
    print()
    print("Will you attract the donkeys, or will Ed Sheeran attract you...?")
    print()
    print("(please stay tuned for a PART 2! electric boogaloo ft. ed sheeran collaborating with justin bieber at the gambling studio for a lucky unicorn!)")
    print()
    return ""


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give:
            if low < response <= high:
               return response
            
            # output an error
            else:
                print(error)

        except ValueError: 
            print(error)


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine goes here...

played_before = yes_no("Have you played this game before?")


if played_before == "no":
    instructions()

print()

print("program continues")

# Ask user how much they want to play with...
how_much = num_check ("How much would you like to play for?", 0, 10)

balance = how_much

rounds_played = 0

play_again = input ("Press <Enter> to play...").lower()
while play_again == "" and balance >= 1:

    # Increase # of rounds played 
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    chosen_num = random.randint(1, 100)
    
    # Adjust balance
    # If the random # is between 1 and 5, user gets an ed sheeran (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "ed sheeran"
        prize_decoration = "!E!"
        balance += 4  
    # If the random # is between 6 and 36, user gets a donkey (subtract $1 to balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1
    # The token is either a horse or a zebra... in both cases, subtract $0.50 from the balance
    else:
        # If the chosen number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"
        # Otherwise, set it to a zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance <=1:
        # If balance is too low, exit the game and output a suitable message
        play_again = "xxx"
        print("Sorry you have run out of money, pay up before ed sheeran shows up in your house tonight")
    else:
        play_again = input ("Press Enter to play again")


    print()

print("we are done")