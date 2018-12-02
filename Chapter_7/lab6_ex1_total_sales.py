# Design a program that asks the user to enter a store's sales for each
# day of the week. The amounts should be stroed in a list. Use a loop to
# calculate the total sales for the week and display the result.

def enterDailySales( daysOfTheWeek ):
    dailySales = []

# Get the sales for each day of the week 
    for currentDay in daysOfTheWeek:
        print( 'Enter sales for', currentDay + ': ', end='' )
        dailySale = float( input() )
        dailySales.append( dailySale )
    return dailySales

# Calculate the total sales for the week
def calculateWeeklySale(dailySales):
    total = 0.0
    for currentDailySale in range( len( dailySales)):
        total = total + dailySales[currentDailySale]
    return total

# Print the report
def printWeeklyReport(daysOfTheWeek, dailySales, totalSales):
    print()
    print('Weekly Sale Report\n------------------')
    print()

    for currentDay in range( len(daysOfTheWeek)):
        print(daysOfTheWeek[currentDay] + "'s sales: ",\
        "$" + format(dailySales[currentDay], '.2f'))

    print()
    print('Total weekly sales: ', "$" + format(totalSales, '.2f'), '\n')

# Define the main function and the main variables
def main():
    daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', \
    'Friday', 'Saturday', 'Sunday']

    dailySales = enterDailySales(daysOfTheWeek) # Daily sales
    totalDailySales = calculateWeeklySale(dailySales) # Weekly sales
    printWeeklyReport(daysOfTheWeek, dailySales, totalDailySales)

# Execute the program
main()
