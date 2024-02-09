# Simulate texting but Crack Chat always insults you.

# Imports.
from pathlib import Path
import json
import random, time

# Load insults.
insults = json.loads(Path('apps/entertainment/insults.json').read_text())

# Load user info.
user_info = json.loads(Path('user_info/user_info.json').read_text())
name = user_info['username']

# Load preferences.
preferences = json.loads(Path('user_info/preferences.json').read_text())
use_name = preferences['Use Name']

# Print an introduction.
print('\nWelcome to Crack Chat!')
time.sleep(1)

# Start the main loop.
while True:

    # Print instructions.
    print('\nEnter your message at the ">>>" prompt.')
    print('Type "quit" to exit.')

    # Get the user's message.
    message = input('\n>>> ')

    # If the user wants to quit, break out of the loop.
    if message == 'quit':
        break

    # Otherwise, print a random insult.
    if use_name.lower() == "true":
        print(f"\n{name}, {random.choice(insults)}")
    else:
        print(f"\n{random.choice(insults)}")

    # Wait a second.
    time.sleep(1)

# Print a goodbye message.
print('\nGoodbye!')