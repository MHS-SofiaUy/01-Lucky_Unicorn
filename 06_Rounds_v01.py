# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input ("Press <Enter> to play...").lower()
while play_again == "" and balance >= 1:

    # Increase # of rounds played 
    rounds_played += 1

    # Print round number
    print("*** Round #{} ***".format(rounds_played))
    balance -=1
    print("Balance: ", balance)
    print()

    play_again = input("Please enter to play again, or 'xxx' to quit")
    

    print()
    print("Final Balance", balance)

    if balance <=1:
        # If balance is too low, exit the game and output a suitable message
        play_again = "xxx"
        print("Sorry you have run out of money, pay up before ed sheeran shows up in your house tonight")


    print()

print("we are done")