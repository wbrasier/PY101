import random

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

def prompt(message):
    print(f"==> {message}")

#User is asked to select a move
def display_instructions():
    instruction = (f'''
    ==> Enter your move!
    ==> 'p' for paper
        'r' for rock
        'sp' for spock
        'sc' for scissors
        'l' for lizard
    ''')
    print(instruction)

def get_user_move():
    choice_letters = input()
    while choice_letters not in VALID_CHOICES:
            prompt("That's not a valid choice.")
            choice_letters = input().lower()

    choice = VALID_CHOICES[choice_letters]
    return choice

def display_winner(player, computer):
    player_beats = WINNING_MOVES[player]
    computer_beats = WINNING_MOVES[computer]
    
    if computer in player_beats:
        prompt("You win!")
    elif player in computer_beats:
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

# main game play loop
while True:
    display_instructions()
    
    
    player_choice = get_user_move()
    
    # computer selects a move randomly
    computer_choice = random.choice(list(VALID_CHOICES.values()))
    
    # tells the user what was chosen
    prompt(f"You chose {player_choice}, computer chose {computer_choice}.")
    
    display_winner(player_choice, computer_choice)

    # asks if the user wants to play again and breaks if n is entered
    prompt("Do you want to play again? (y/n)")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt('Please enter "y" or "n".')
        answer = input().lower()
    if answer[0] == 'n':
        break