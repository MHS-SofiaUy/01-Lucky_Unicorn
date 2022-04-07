import random

# Main routine goes here

tokens = ["zebra", "horse", "donkey", "ed sheeran"]
balance = 100

# Testing loop to generate 20 tokens
for item in range (0,100):
    chosen = random.choice(tokens)
    
    # Adjust balance
    if chosen == "ed sheeran":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    # output
    print("Token: {} , Balance ${}".format(chosen, balance))





