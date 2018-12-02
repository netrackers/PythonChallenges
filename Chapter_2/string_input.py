# Get the user's first name
first_name = input('Enter your first name: ')

# Get the user's last name
last_name = input('Enter your last name: ')

# Print a greeting to the user
print('Hello', first_name, last_name)

# Reading numbers with the input function
string_value = input('How many hours did you work? ')
hours = int(string_value)
print('You have worked ', hours, 'hours this week.')

# Nested function calls
hours = int(input('How many hours did you reallllly work? '))
print('Wow!', hours, "hours is a lot in a week!")
print()
pay_rate = float(input('What is your hourly pay rate? '))
print("That's not too bad!")
print("So you've made", hours*pay_rate, "this week")