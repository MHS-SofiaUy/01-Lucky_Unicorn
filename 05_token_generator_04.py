import random

# Main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range (0,10):
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
print()

print()
print("Starting Balance: ${}".format(STARTING_BALANCE))
print("Final Balance: ${}".format(balance))



