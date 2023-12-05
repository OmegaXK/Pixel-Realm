"""A simple rock-paper-scissors game."""

# Imports.
import random, time, sys

# Constants.
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
CHOICES = [ROCK, PAPER, SCISSORS]

TIE = 'tie'
PLAYER_WINS = 'player_wins'
COMPUTER_WINS = 'computer_wins'


def get_player_choice():
    """Return the player's choice."""

    # Print out the choices.
    time.sleep(1)
    print('\nMake your decision:')
    print('\n[r] Rock')
    print('[p] Paper')
    print('[s] Scissors')

    # Let the player choose an option.
    player_choice = ''
    while True:
        player_choice = input('Input the letter for your choice (r, p, s): ')
        player_choice = player_choice.lower()

        if player_choice != 'r' and player_choice != 'p' \
            and player_choice != 's':

            # The player didn't choose rock, paper, or scissors.
            print('\nPlease type "r", "p", or "s".')

        else:
            # The player chose a correct option.
            break

    # Convert the player's choice to a constant.
    if player_choice == 'r':
        player_choice = ROCK
    elif player_choice == 'p':
        player_choice = PAPER
    elif player_choice == 's':
        player_choice = SCISSORS

    # Return the player's choice.
    return player_choice


def get_computer_choice():
    """Get the computer's choice."""

    # Randomly generate a comqputer choice.
    computer_choice = random.choice(CHOICES)
    return computer_choice


def evaluate_result(player_choice, computer_choice):
    """Figure out who won the round based on the choices."""

    if player_choice == computer_choice:
        # It was a tie.
        return TIE
    
    # Check for outcomes where the player wins.
    elif player_choice == ROCK and computer_choice == SCISSORS:
        return PLAYER_WINS
    
    elif player_choice == PAPER and computer_choice == ROCK:
        return PLAYER_WINS
    
    elif player_choice == SCISSORS and computer_choice == PAPER:
        return PLAYER_WINS
    
    # If none of the above outcomes occurred, the computer won.
    else:
        return COMPUTER_WINS
    

def play_again():
    """Print out the current scores, and ask the player if they would
    like to play again."""

    time.sleep(2.5)
    print('\nWould you like to play another round? (yes/no)')
    
    # Get the player's choice.
    while True:
        play_again = input('> ')
        play_again = play_again.lower()

        if play_again == 'yes':
            # The player wants to play again.
            return True

        elif play_again == 'no':
            # The player doesn't want to play again.
            return False

        else:
            # The player didn't enter a valid choice.
            print('\nPlease type "yes" or "no".')


def main():
    """Rock Paper Scissors main code."""

    # Reset the scores.
    player_score = 0
    computer_score = 0

    # Print the introduction.
    print('\nWelcome to Rock-Paper-Scissors!')
    time.sleep(1)
    input('Press enter when you are ready to play: ')

    # Game loop.
    while True:

        # Play the round.
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        outcome = evaluate_result(player_choice, computer_choice)

        # Figure out who won.
        if outcome == PLAYER_WINS:
            time.sleep(1)
            print(f'\nYou chose {player_choice}.')

            time.sleep(1)
            print(f'The computer chose {computer_choice}.')

            time.sleep(1.5)
            print('\nYou beat the computer!')

            player_score += 1

        elif outcome == COMPUTER_WINS:
            time.sleep(1)
            print(f'\nYou chose {player_choice}.')

            time.sleep(1)
            print(f'\nThe computer chose {computer_choice}.')

            time.sleep(1.5)
            print('\nThe computer destroyed you!')

            computer_score += 1

        elif outcome == TIE:
            time.sleep(1)
            print(f'\nYou chose {player_choice}.')

            time.sleep(1)
            print(f'The computer chose {computer_choice}.')

            time.sleep(1.5)
            print('It was a tie! Nobody gets a point.')

        # Print out the current scores.
        time.sleep(2)
        print(f'\nThe player has {player_score} points.')
        print(f'The computer has {computer_score} points.')

        # Ask the player if they want to play again.
        if play_again() != True:
            return


main()
print('\nThank you for playing!')
sys.exit()