# This program calculates the sum of bugs collected over a 5 days period. 
MAX = 5 # Numbers of days 
# Initialize an accumulator variable
total = 0.0

# Get the number of bugs per day
for counter in range(MAX):
    # Get the number of bugs for each day
    number = int(input('Enter the number of bugs for: '))
    total = total + number

# Display the total of bugs collected
print('The total is', total)