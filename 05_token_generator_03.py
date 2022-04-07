import random

# Main routine goes here

tokens = ["zebra", "horse", "donkey", "ed sheeran"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range (0,500):
    chosen = random.choice(tokens)
    
    # Adjust balance
    if chosen == "ed sheeran":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

print()
print("Starting Balance: ${}".format(STARTING_BALANCE))
print("Final Balance: ${}".format(balance))



