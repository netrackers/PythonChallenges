# This program calculates the numbers of calories burned while exercising

# Define the time range and increment
START_TIME = 10
END_TIME = 35
INCREMENT = 5
CALORIES_BURNED = 4.2

# Print the table headings
print() # Creates a space befor the table header
print('Minutes\tCalories Burned')
print('------------------------')

# Print the speeds
for duration in range (START_TIME, END_TIME, INCREMENT):
    calories = duration * CALORIES_BURNED
    print(duration,'\t', calories)

print() # Adds a space at the end of the script