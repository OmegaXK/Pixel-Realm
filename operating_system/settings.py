"""The program that lets the user change their settings."""

from pathlib import Path
from time import sleep
import json


def main():
    """The main function for the settings program."""

    # Load in the user's data.
    path = Path('user_info/user_info.json')
    string = path.read_text()
    user_data = json.dumps(string)

    # Print the user's current data.
    print('This is your current information: ')
    print(f"[1] Username: {user_data['username']}")
    print(f"[2] Email: {user_data['email']}")
    print(f"[3] Password: {user_data['password']}")

    print("Input the respective key to change any of your data. (1, 2, 3)")
    print('Input "exit" to quit out of the settings.')

    choice = ''
    while choice != '1' and choice != '2' and choice != '3' \
        and choice != 'exit':
        choice = input('[?] ')
        