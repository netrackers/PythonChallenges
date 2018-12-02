# Get the user's information
name = input('What is your name? ')
hours_worked = float(input('How many hours did your work this week? '))
pay_rate =float(input('What is your hourly wage? '))
week_earnings = hours_worked * pay_rate

# Display the information to the user
print('Welcome to Regebox', name, '!')
print('Congratulations! This week you have made a total of', week_earnings,)
print(week_earnings, 'Has been deposited into your account')
print('Congratulations on a job well done!')