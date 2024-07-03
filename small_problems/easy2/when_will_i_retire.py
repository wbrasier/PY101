import datetime

current_age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))

current_year = datetime.date.today().year
years_of_work_left = retirement_age - current_age
retirement_year = current_year + years_of_work_left

print(f'''
It's {current_year}. You will retire in {retirement_year}.
You have only {years_of_work_left} years of work to go!''')