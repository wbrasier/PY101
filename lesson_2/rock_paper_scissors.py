import random
import os

VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock',
    }

WINNING_MOVES = {
    'rock': ['lizard', 'scissors'],
    'lizard': ['paper', 'spock'],
    'spock': ['scissors', 'rock'],
    'scissors': ['paper', 'lizard'],
    'paper': ['rock', 'spock'],
}

ROUNDS = 5
POINTS_TO_WIN = (ROUNDS // 2) + 1

# functions that deal with input from user that is less specific
def prompt(message):
    print(f"==> {message}")

def fix_input(data):
    data = data.lower().replace(" ", "")
    return data

def convert_letters(option):
    if len(option) <= 2:
        option = VALID_CHOICES[option]
    return option

# Functions that display to the terminal
def display_welcome():
    prompt('Welcome to Rock, Paper, Scissors, Spock, Lizard!')
    prompt(f'The best out of {ROUNDS} rounds wins!')

def display_rules():
    print('''
    Scissors cuts Paper
    Paper covers Rock
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissors
    Scissors decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock
    Rock Crushes Scissors
    ''')

#User is asked to select a move
def display_instructions():
    instruction = '''
==> Enter your move!
==> 'p' for paper
    'r' for rock
    'sp' for spock
    'sc' for scissors
    'l' for lizard
    '''
    print(instruction)

def display_current_scores(computer, player):
    print(f"computer: {computer}   player: {player}")

def display_choices(computer, player):
    prompt(f"You chose {player}, computer chose {computer}.")

def display_round_winner(champ):
    match champ:
        case 'player':
            prompt('You win!')
        case 'computer':
            prompt('Computer wins!')
        case False:
            prompt('Tie!')

def display_champ(champion):
    match champion:
        case 'player':
            prompt('Good game! The champion is YOU!')
        case 'computer':
            prompt('The champion is the computer. Better luck next time!')

# Functions that get input and return it
# Returns True if yes, False if no
def get_yes_or_no(question):
    prompt(question)
    answer = input()
    answer = fix_input(answer)
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt('Please enter "y" or "n".')
        answer = input()
        answer = fix_input(answer)
    if answer[0] == 'n':
        return False
    return True

def get_user_move():
    choice = input()
    choice = fix_input(choice)

    while (choice not in VALID_CHOICES and
    choice not in list(VALID_CHOICES.values())):
        prompt("That's not a valid choice.")
        if choice.startswith('s'):
            prompt("Did you mean 'sc' for scissors or 'sp' for spock?")
        choice = input()
        choice = fix_input(choice)

    return convert_letters(choice)

def get_computer_move():
    return random.choice(list(VALID_CHOICES.values()))

# Analyze the score functions
def determine_round_winner(player, computer):
    player_beats = WINNING_MOVES[player]
    computer_beats = WINNING_MOVES[computer]

    if computer in player_beats:
        return 'player'
    if player in computer_beats:
        return "computer"
    return False

def check_for_champ(points):
    if points['player'] == POINTS_TO_WIN:
        return 'player'
    if points['computer'] == POINTS_TO_WIN:
        return 'computer'
    return False

def increment_scores(winner):
    if winner:
        scores[winner] += 1

# main game play function
def rps_game(points):
    # round loop that continues until somebody wins (best of ROUNDS)
    while True:
        display_current_scores(points['computer'], points['player'])

        display_instructions()

        player_choice = get_user_move()

        computer_choice = get_computer_move()

        os.system('clear')

        display_choices(computer_choice, player_choice)

        # determines winner and displays who won
        winner = determine_round_winner(player_choice, computer_choice)
        display_round_winner(winner)

        increment_scores(winner)

        # exits the loop if somebody has reached POINTS_TO_WIN
        champion = check_for_champ(points)
        if champion:
            display_current_scores(points['computer'], points['player'])
            display_champ(champion)
            break

os.system('clear')
display_welcome()

if get_yes_or_no("Do you want to view the rules? (y/n)"):
    display_rules()
    input('Hit the Enter key to continue.')

# Loop that continues until the user doesn't want to play again
while True:
    os.system('clear')
    # initializes scores at 0 for computer and player
    scores = { 'player' : 0, 'computer': 0}
    rps_game(scores)
    if not get_yes_or_no("Do you want to play again? (y/n)"):
        prompt('Thanks for playing!')
        break