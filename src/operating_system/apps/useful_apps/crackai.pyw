
"""Code for Crack AI."""

import random, time, os, json
from pathlib import Path

# Set up the path.
resource_path = os.path.join(os.path.dirname(__file__), '')
rp = resource_path.replace('operating_system/apps/useful_apps', 'operating_system/')

# Get the info.
user_info = json.loads(Path(f'{rp}user_info/user_info.json').read_text())
preferences = json.loads(Path(f'{rp}user_info/preferences.json').read_text())

def main():
    """Main crack AI code."""

    name, use_name = load_name()

    print("")
    if use_name.lower() == "true":
        print(f"Welcome to Crack AI {name}. I am here to help you with any of your questions.")
    else:
        print(f"Welcome to Crack AI. I am here to help you with any of your questions.")

    time.sleep(1)
    
    while True:
        print("")
        print("AI Options:")
        print("[1] Yes / No Questions")
        print("[2] Open Ended Questions")
        print("[q] Quit Program")

        chosen_option = input(">>> ")

        if chosen_option == "1":
            time.sleep(1)
            yesno_questions()

        elif chosen_option == "2":
            time.sleep(1)
            open_ended()

        elif chosen_option.lower() == "q":
            return


def open_ended():
    """Let the user enter open ended questions."""

    possible_answers = ['Um idk about that one. Ask me a different question.',
                        'System error, try again later.',
                        'Internal server error, try again later.',
                        'Processing error, try again later.',
                        'Do I look like ChatGPT? I ain\'t tryna answer no question.',
                        "Do your homework on your own.",
                        "If you can't be bothered to think on your own, why should I?",
                        ]

    while True:
        
        print("")
        print("Enter your open ended question, and I will accurately answer you.")
        print('Enter "quit" to return to the main menu.')
        question = input(">>> ")

        if question.lower() != "quit":
            time.sleep(random.randint(1, 8))
            print("")
            print(str(random.choice(possible_answers)))

        else:
            return                       


def yesno_questions():
    """Let the user enter yes or no questions."""

    possible_answers = ['Yes', 'No', 'Sometimes', 'Processing error, please try again.']

    while True:

        print("")
        print("Enter your yes or no question, and I will correctly answer you.")
        print('Enter "quit" to return to the main menu.')
        question = input(">>> ")

        if question.lower() != "quit":
            time.sleep(random.randint(1, 6))
            print(str(random.choice(possible_answers)))

        else:
            return
    

def load_name():
    """Load the user's name."""

    name = user_info['username']
    use_name = preferences['Use Name']
    return name, use_name


# Testing.
if __name__ == "__main__":
    main()
    print("")
    print("Goodbye!")
