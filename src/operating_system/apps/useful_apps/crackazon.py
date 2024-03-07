"""Crackazon, the ultimate online shopping center!!"""

# Totally not a ripoff of Amazon. (it's a ripoff of Amazon)

# Basically it just prompts you to type in what you want to buy,
#  and then it tells you you're too poor to buy it.

# Imports.
import random, sys, time

# Define the responses.
responses = ['you need money to buy that!', "you're too poor",
             "you need money", "you can't aford that", "you're broke",
             "you can't buy things if you don't have money!",
             "imagine being poor", "imagine being broke",
             "stop trying to buy things, you poor person",
             "get money", "get a job"]

# Run the main loop.
while True:

    # Prompt the user to type what they want to buy.
    print('\n\nType in what you would like to purchase, and press enter.')
    print('Type in "quit" to exit the program.')

    answer = input('\n>>> ')

    if answer == 'quit':
        break

    # Insult the user.
    print(f"\n{random.choice(responses)}")

    time.sleep(2)

sys.exit()