# Chapter 3 - Exercice 1: Day of the weekk
# Write a program that asks the user for a number in the range of 1 through 7.
# The program should display the corresponding day of the week,
# Where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday,
# 6 = Saturday, and 7 = Sunday. The program should display an error message
# if the user enters a number that is outside the range of 1 through 7

user_number = int( input('Please enter a number between 1 and 7: ') ) # Get a number from the user

# Verify that user enter a good number and displays the corresponding day.
if user_number == 1:
    print( str(user_number) + ' = Monday')
elif user_number == 2:
    print( str(user_number) + ' = Tuesday' )
elif user_number == 3:
    print( str(user_number) + ' = Wednesday' )
elif user_number == 4:
    print( str(user_number) + ' = Thursday' )
elif user_number == 5:
    print( str(user_number) + ' = Friday' )
elif user_number == 6:
    print( str(user_number) + ' = Saturday' )
elif user_number == 7:
    print( str(user_number) + ' = Sunday' )
else:
    print( str(user_number) + ' is not a number between 1 and then. Please'\
    ' enter a new number.')
    