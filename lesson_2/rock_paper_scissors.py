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

def prompt(message):
    print(f"==> {message}")

def display_welcome():
    prompt('Welcome to Rock, Paper, Scissors, Spock, Lizard!')
    prompt(f'The best out of {ROUNDS} rounds wins!')

# Returns True if yes, False if no
def yes_or_no(question):
    prompt(question)
    answer = input().lower()
    answer = answer.replace(" ", "")
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt('Please enter "y" or "n".')
        answer = input().lower()
    if answer[0] == 'n':
        return False
    return True

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

def get_user_move():
    choice_letters = input().lower()
    choice_letters = choice_letters.replace(" ", "")
    print(VALID_CHOICES)
    print(choice_letters not in VALID_CHOICES)
    while (choice_letters not in VALID_CHOICES and 
    choice_letters not in list(VALID_CHOICES.values())):
        prompt("That's not a valid choice.")
        choice_letters = input().lower()
        choice_letters = choice_letters.replace(" ", "")
    
    if len(choice_letters) <= 2:
        choice = VALID_CHOICES[choice_letters]
    else:
        choice = choice_letters
    return choice

def determine_round_winner(player, computer):
    player_beats = WINNING_MOVES[player]
    computer_beats = WINNING_MOVES[computer]

    if computer in player_beats:
        return 'player'
    if player in computer_beats:
        return "computer"
    return False

def display_round_winner(champ):
    match champ:
        case 'player':
            prompt('You win!')
        case 'computer':
            prompt('Computer wins!')
        case False:
            prompt('Tie!')

def check_for_champ(points):
    if points['player'] == POINTS_TO_WIN:
        return 'player'
    if points['computer'] == POINTS_TO_WIN:
        return 'computer'
    return False

def display_champ(champion):
    match champion:
        case 'player':
            prompt('Good game! The champion is YOU!')
        case 'computer':
            prompt('The champion is the computer. Better luck next time!')

# main game play function
def rps_game(points):
    # round loop that continues until somebody wins (best of ROUNDS)
    while True:
        display_instructions()

        player_choice = get_user_move()

        # computer selects a move randomly
        computer_choice = random.choice(list(VALID_CHOICES.values()))

        os.system('clear')

        # tells the user what was chosen
        prompt(f"You chose {player_choice}, computer chose {computer_choice}.")

        # determines winner and displays who won
        winner = determine_round_winner(player_choice, computer_choice)
        display_round_winner(winner)

        # updates the scores
        if winner:
            points[winner] += 1
        print(f"computer: {points['computer']}   player: {points['player']}")

        champion = check_for_champ(points)
        if champion:
            display_champ(champion)
            break

os.system('clear')
display_welcome()

if yes_or_no("Do you want to view the rules? (y/n)"):
    display_rules()

# Loop that continues until the user doesn't want to play again
while True:
    os.system('clear')
    # initializes scores at 0 for computer and player
    scores = { 'player' : 0, 'computer': 0}
    rps_game(scores)
    if not yes_or_no("Do you want to play again? (y/n)"):
        prompt('Thanks for playing!')
        break