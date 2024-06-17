import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f"==> {message}")

# decides and displays winner based on conditions
def display_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')):
        prompt("You win!")
    elif ((player == 'rock' and computer == 'paper') or
        (player == 'paper' and computer == 'scissors') or
        (player == 'scissors' and computer == 'rock')):
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