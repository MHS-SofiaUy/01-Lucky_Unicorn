import random

# set balance for testing purposes
balance = 5

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
        balance += 4  
    # If the random # is between 6 and 36, user gets a donkey (subtract $1 to balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        # If the chosen number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
        # Otherwise, set it to a zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

    if balance <=1:
        # If balance is too low, exit the game and output a suitable message
        play_again = "xxx"
        print("Sorry you have run out of money, pay up before ed sheeran shows up in your house tonight")
    else:
        play_again = input ("Press Enter to play again")


    print()

print("we are done")