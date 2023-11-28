"""Contains the main functions to login and create an account for the
Pixel Realm OS."""

# The file that lets the user login and create an account for the Pixel 
# Realm OS.

import sys, os
from pathlib import Path
import json

def sign_up():
    """Creates a new account for the user."""
    
    # Let the user enter their username and email.
    username = input("\nEnter a username: ")
    email = input("Enter your email: ")

    # Let the user enter their password. Make sure that the password and
    # confirm_password are the same.
    password, confirm_password = '0', '1'
    while password != confirm_password:
        password = input("Enter a password: ")
        confirm_password = input("Confirm your password: ")

        if password != confirm_password:
            print("\nYour passwords do not match. Please try again.")

    # Create a dictionary for the user's information.
    user_info = {"username": username, "email": email, "password": password}

    # Create a new file for the user's information.
    path = Path('user_info/user_info.json')
    path.write_text(json.dumps(user_info))

    # Let the user know that their account was created.
    print("\nYour account was succsesfully created.")
    print("You can now login.")

    return


def login():
    """Lets the user login to their account."""

    # Let the user enter their username and password.
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    # Open the file that contains the user's information.
    path = Path('user_info/user_info.json')
    user_info = json.loads(path.read_text())

    # Check if the user's username and password are correct.
    if username == user_info['username'] and password == user_info['password']:
        print("\nYou have successfully logged in.")
        return True
    else:
        print("\nYour username or password is incorrect.")
        return False


def main():
    """Main function for the login page."""

    while True:
        # Let the user choose if they want to signup, login, or exit.
        print("\n\nWelcome to the Pixel Realm OS.")

        print('\n[1] Sign up')
        print('[2] Login')
        print('[3] Exit')

        choice = input("\nWhat would you like to do? [1, 2, 3]: ")

        # Check if the user wants to signup, login, or exit.
        if choice == '1':
            sign_up()
        elif choice == '2':
            if login() == True:
                return True
        elif choice == '3':
            return False
        

# If the file is run directly, run the main function. (For testing)
if __name__ == '__main__':
    main()