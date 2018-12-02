# Get the desired future value
future_value = float(input('Enter the desired future vaalue: '))

# Get the annual interest rate
rate = float(input('Enter the annual interest rate: '))

# Get the number of years that the money will appreciate
years = int(input('Enter the number of years the money will grow: '))

# calculate the amount needed to deposit
present_value = future_value / (1.0 + rate) ** years

# Display the amount to deposit
print('You will need to deposit this amount: ', present_value)