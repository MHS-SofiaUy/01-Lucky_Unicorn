import random

# Main routine goes here

tokens = ["zebra", "horse", "donkey", "ed sheeran"]

# Testing loop to generate 20 tokens
for item in range (0,20):
    chosen = random.choice(tokens)
    print(chosen, end='\t')





