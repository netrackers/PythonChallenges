# This program calculates the total of bugs collected over a 5 days period

# Set the number of days
collection_days = 5

# Initialize an accumulator for the number of bugs
total = 0.0

# Prompt user to enter the number of bugsg for each day
print()
for days in range(collection_days):
    print('Number of bugs for day', days + 1, end='')
    # Store the value in the number variable before processing
    number = int(input(': '))
    # Add the number to the accumulator
    total += number

# Display the total number of bugs
print()
print('Number of bugs collected for the last 5 days: ', total)
print()