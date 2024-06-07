# Get input from user
#   loan amount
#   APR (annual percentage rate)
#   loan duration
# calculate the monthly payment
#   calculate the monthly interest rate (APR / 12)
#   calculate the loan duration in months


def prompt(message):
    print(f'=> {message}')
    return f'=> {message}'

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

# returns False if the apr is valid, otherwise it is invalid and returns True
def invalid_num(apr_input):
    try:
        float(apr_input)
    except ValueError:
        return True

    return False

# returns False if the years and months are whole numbers, otherwise True
def invalid_length(length):
    try:
        int(length)
    except ValueError:
        return True

    return False

prompt("Welcome to the loan calculator!")

# Asks user for loan amount
prompt("What amount is your loan in dollars?")
total = input("=> Loan amount : ")

while invalid_num(total):
    prompt("Hmm... that is not a valid input. Please enter your loan amount.")
    prompt("Example: Loan amount of $42,318.50 entered as 42318.50")
    total = input("=> Loan amount: ")

# Asks user for APR (annual percentage rate) and calculates monthly APR
prompt("What is the APR (Annual Percentage Rate) of the loan?")
prompt("Example: 4.8% gets entered as 4.8")
apr = input("=> APR: ")

while invalid_num(apr):
    prompt("Hmm... that is not a valid input. Enter your apr as a number.")
    prompt("Example: .25% gets entered as .25 or 0.25")
    apr = input("=> APR: ")

if apr != 0:
    apr_monthly = (float(apr)/100) / 12
else:
    apr_monthly = apr

# Asks user for loan duration in years and months and calculates it in months
prompt("What is the duration of your loan in years? Months?")
years = input("=> Years: ")

while invalid_length(years):
    prompt("Hmm... that is not a valid input. Enter a whole number for years.")
    years = input("=> Years: ")

months = input("=> Months: ")

while invalid_length(months):
    prompt("Hmm.. that is not a valid input. Enter a whole number for months.")
    months = input("=> Months: ")


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