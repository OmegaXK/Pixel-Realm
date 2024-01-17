"""Contains the main functions to login and create an account for the
Pixel Realm OS."""

# The file that lets the user login and create an account for the Pixel 
# Realm OS.

from pathlib import Path
from time import sleep
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
            sleep(1)
            print("\nYour passwords do not match. Please try again.")

    # Create a dictionary for the user's information.
    user_info = {"username": username, "email": email, "password": password}

    # Create a new file for the user's information.
    path = Path('user_info/user_info.json')
    path.write_text(json.dumps(user_info))

    # Let the user know that their account was created.
    sleep(1)
    print("\nYour account was succsesfully created.")
    print("You can now login.")
    sleep(1)

    return


def login():
    """Lets the user login to their account."""

    # Open the file that contains the user's information.
    path = Path('user_info/user_info.json')

    # Check if the player actually has an account.
    if not path.exists():
        print("\nYou need to make an account before you log in.")
        sleep(1)
        return

    # Let the user enter their username and password.
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    # Load in the user's information.
    user_info = json.loads(path.read_text())

    # Check if the user's username and password are correct.
    if username == user_info['username'] and password == user_info['password']:
        sleep(1)
        print("\nYou have successfully logged in.")
        return True
    else:
        sleep(1)
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

        choice = ''
        while choice != '1' and choice != '2' and choice != '3':
            choice = input("\nWhat would you like to do? [1, 2, 3]: ")

            # Check if the user wants to signup, login, or exit.
            if choice == '1':
                sign_up()
            elif choice == '2':
                if login() == True:
                    return True
            elif choice == '3':
                return False
            else:
                print('Please enter 1, 2, or 3.')
        

# If the file is run directly, run the main function. (For testing)
if __name__ == '__main__':
    main()