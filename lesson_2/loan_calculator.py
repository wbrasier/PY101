# Get input from user
#   loan amount
#   APR (annual percentage rate)
#   loan duration
# calculate the monthly payment
#   calculate the monthly interest rate (APR / 12)
#   calculate the loan duration in months
import os
import sys

def prompt(message):
    print(f'=> {message}')
    return f'=> {message}'

# asks user for loan amount until valid input, and returns loan amount
def request_loan_amount():
    prompt("What amount is your loan in dollars?")
    total_loan = input("=> Loan amount : ")

    while invalid_num(total_loan):
        prompt("That is not a valid input. Please enter the loan amount.")
        prompt("Example: Loan amount of $42,318.50 entered as 42318.50")
        total_loan = input("=> Loan amount: ")
    return total_loan

# calculates the total loan duration in months
def calc_total_months(dur_years, dur_months):
    return (dur_years * 12) + dur_months

# calculates monthly payment
def monthly_payment(loan_amount, monthly_int_rate, loan_dur):
    if monthly_int_rate == 0:
        monthly_cost = loan_amount / loan_dur
    else:
        monthly_cost = (loan_amount * (monthly_int_rate /
            (1 - (1 + monthly_int_rate) ** (-loan_dur))))
    return monthly_cost

# returns False if the apr is a float greater than or equal to 0
def invalid_num(apr_input):
    try:
        float(apr_input)
    except ValueError:
        return True
    if float(apr_input) < 0:
        return True
    return False

# returns False if the years and months are whole numbers larger than 0
def invalid_length(length):
    try:
        int(length)
    except ValueError:
        return True
    if int(length) < 0:
        return True
    return False

def request_length_of_time(unit):
    time_length = input(f"=> {unit}: ")

    while invalid_length(time_length):
        prompt("That is not a valid input. Enter a whole number.")
        time_length = input(f"=> {unit}: ")
    return time_length

# Asks user for APR (annual percentage rate) and calculates monthly APR
def request_apr():
    prompt("What is the APR (Annual Percentage Rate) of the loan?")
    prompt("Example: 4.8% gets entered as 4.8")
    apr_input = input("=> APR: ")

    while invalid_num(apr_input):
        prompt("That is not a valid input. Enter your apr as a number.")
        prompt("Example: .25% gets entered as .25 or 0.25")
        apr_input = input("=> APR: ")
    return apr_input

# asks if the user wants to calculate again. If not the program will exit
def again():
    prompt('Would you like to calculate another loan? Enter y or n.')
    answer = input('=> ')

    while True:
        answer = answer.lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            prompt('Goodbye, thanks for calculating loans with me!')
            sys.exit(0)
        else:
            prompt('That is not a valid input. Enter y for yes or n for no.')
            answer = input('=> ')

prompt("Welcome to the loan calculator!")

# main loan calculator loop
while True:
    os.system('clear')

    total = request_loan_amount()

    apr = request_apr()

    if apr != 0:
        apr_monthly = (float(apr)/100) / 12
    else:
        apr_monthly = apr

    prompt("What is the duration of your loan in years? Months?")
    years = request_length_of_time('Years')
    months = request_length_of_time('Months')
    loan_dur_months = calc_total_months(int(years), int(months))

    payment = monthly_payment(float(total), apr_monthly, loan_dur_months)
    payment = format(payment, "#.2f")

    output = f'''
    => Your loan of ${total} over {loan_dur_months} months will amount to a monthly payment of ${payment}\n
    => Duration: {loan_dur_months} months\n
    => Monthly interest rate: {format(apr_monthly * 100, "#.2f")}%\n
    => Monthly payment: ${payment}\n
     '''
    print(output)
    again()