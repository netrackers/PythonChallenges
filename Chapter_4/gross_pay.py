# This program displays gross pay
# GEt the number of hours worked
hours = int(input('Enter the hours worked this week: '))
while hours < 1 or hours > 40:
    print('Error: The hours worked cannot be less that one or more than 40.')
    hours = int(input('Enter the hours worked this week: '))

# Get the hourly rate
pay_rate = float(input('Enter the hourly pay rate: '))

# Calculate the gross pay
gross_pay = hours * pay_rate

# Display the gross pay.
print('Gross pay: $', format(gross_pay, ',.2f'))