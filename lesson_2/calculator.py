# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
#   bonus feature: extract messages to a configuration file and access by key
# Perform the operation on the two numbers.
# Print the result to the terminal.
#   bonus feature: ask the user for another calculation
import json
import sys

# opens json file with text as json object and stores it as dict
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'=> {message}')

# Checks to see if the input is an integer
def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

# Asks the user if they want to calculate again, exits the program if not
def again():
    prompt(MESSAGES['again?'])
    while True:
        answer = input().capitalize()
        if answer in ('Y', 'Yes'):
            return True
        if answer in ('N', 'No'):
            prompt(MESSAGES['goodbye'])
            sys.exit(0)
        else:
            prompt(MESSAGES['invalid again'])

# main calculate function
def calculate():
    # Ask the user for the first number
    prompt(MESSAGES['first num'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['not valid num'])
        number1 = input()

    prompt(MESSAGES['second num'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['not valid num'])
        number2 = input()

    prompt(MESSAGES['which op'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(MESSAGES['invalid op'])
        operation = input()

    match operation:
        case '1': # '1' represents addition
            output = int(number1) + int(number2)
        case '2': # '2' represents subtraction
            output = int(number1) - int(number2)
        case '3': # '3' represents multiplication
            output= int(number1) * int(number2)
        case '4': # '4' represents division
            output = int(number1) / int(number2)

    prompt(f"{MESSAGES['result']}{output}")

# Main calculator code
prompt(MESSAGES['welcome'])

calculate()

while True:
    again()
    calculate()