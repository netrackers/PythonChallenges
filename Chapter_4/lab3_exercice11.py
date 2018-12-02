# This program calculates the sleep debt of a user

# Set the number of days
SLEEP_DAYS = 7
DESIRABLE_HOURS = 8
MAX_SLEEP_HOURS = SLEEP_DAYS * 8


# Initialize an accumulator for the number of bugs
total = 0.0

# Prompt user to enter the number of bugsg for each day
print()
for days in range(SLEEP_DAYS):
    print('Number of sleep hours for day', days + 1, end='')
    # Store the value in the number variable before processing
    number = int(input(': '))
    # Add the number to the accumulator
    total += number
print()
print('Number of sleep hours for the last 7 days: ', total)

if total >= MAX_SLEEP_HOURS:
    print('Congratulation, you have met or exceeded the desirable number of sleep hours ')
    print()
else:
    print('You need to work on your sleep schedule')
    print()
