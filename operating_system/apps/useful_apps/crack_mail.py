"""Crack Mail, it's like email, but Crack!"""

# Imports.
from time import sleep

"""
The EMAILS dictionary stores your emails in this form:
- Every key is the email's subject
- Every value is the email's contents.
"""

EMAILS = {
    "[1] Crack": "Crack is very good.",
    "[2] Crack Deals": "Buy our Crack because it's good.",
    "[3] Try Crack": "You should try Crack!",
    "[4] You Need Crack": "We highly recommend Crack.",
    "[5] Discount Crack": "Our Crack deals are the best,"
}


def print_emails():
    """Print out the user's current unread emails. The counter variable
    keeps track of what email we are on currently."""

    print("\n\n\nUnread Emails:\n")

    for subject in EMAILS.keys():

        print(f'{subject}\n')


def read_emails():
    """Let the user read their emails."""

    # Get the user's choice of what they want to read.
    while True:
        response = input("\nType the email you want to read. (1 - 5): ")

        if response in ["1", "2", "3", "4", "5"]:
            break 
        else:
            print('Please enter a number between 1 and 5.')
            sleep(1)

    # Figure out which email to print the contents of.
    for subject, contents in EMAILS.items():

        if subject.startswith(f'[{response}]'):

            # Print this email.
            print(f'\n\n{subject}:')
            print(f'\n{contents}')
            sleep(3)

            # Let the user read the email.
            input("\nPress enter to continue: ")


# Main game looop.
while True:
    print_emails()
    read_emails()