"""The program that lets the user change their settings."""

from pathlib import Path
from time import sleep
import json, sys


def main():
    """The main function for the settings program."""

    # Load in the user's data.
    path = Path('user_info/user_info.json')
    string = path.read_text()
    user_data = json.dumps(string)

    # Define the user's data.
    username = user_data['username']
    email = user_data['email']
    password = user_data['password']

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

        if choice == '1':
            username = get_new_username()
            save_new_data(username)

        elif choice == '2':
            email = get_new_email()
            save_new_data(email)

        elif choice == '3':
            password = get_new_password()
            save_new_data([password])

        elif choice == 'exit':
            sys.exit()

        else:
            print('Please enter 1, 2, 3, or "exit".')


def save_new_data(new_data):
    """Save the user's recent data."""




def get_new_password():
    """Let the user enter a new password."""

    while True:
        password = input('Please enter a new password: ')
        confirm_password = input('Please confirm your password: ')

        if password == confirm_password:
            break
        else:
            sleep(1)
            print('Your passwords do not match.')
            return False
    
    sleep(1)
    print('Your password has been changed succsesfully.')
    return password


def get_new_username():
    """Prompts the user to enter a new username."""

    new_username = input('\nPlease enter a new username: ')
    sleep(1)
    return new_username


def get_new_email():
    """Prompts the user to enter a new email."""

    new_email = input('\nPlease enter a new email: ')
    sleep(1)
    return new_email