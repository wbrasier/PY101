import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

WINNING_MOVES = {
    'rock': ['lizard', 'scissors'],
    'lizard': ['paper', 'spock'],
    'spock': ['scissors', 'rock'],
    'scissors': ['paper', 'lizard'],
    'paper': ['rock', 'spock'],
}

def prompt(message):
    print(f"==> {message}")

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
    #User is asked to select a move
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()
    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        choice = input()
    
    # computer selects a move randomly
    computer_choice = random.choice(VALID_CHOICES)
    
    # tells the user what was chosen
    prompt(f"You chose {choice}, computer chose {computer_choice}.")
    
    display_winner(choice, computer_choice)

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