#                           Exercice 15 - Time Calculator
#
#  Write a program that asks the user to enter a number of seconds and works as follows:
#
#   • There are 60 seconds in a minute. If the number of seconds entered by the user is greater
#   than or equal to 60, the program should convert the number of seconds to minutes and
#   seconds.
#   • There are 3,600 seconds in an hour. If the number of seconds entered by the user is
#   greater than or equal to 3,600, the program should convert the number of seconds to
#   hours, minutes, and seconds.
#   • There are 86,400 seconds in a day. If the number of seconds entered by the user is
#   greater than or equal to 86,400, the program should convert the number of seconds to
#   days, hours, minutes, and seconds.

print()
userSeconds = int( input( 'Please enter the number of seconds to convert: ')) # Get the number of seconds from the user

# Process the number entered by the user.
days = int( userSeconds / 86400) # Convert the number to days
hours = int( ( (userSeconds % 86400) / 3600) ) # Convert the remainder of the previous operation to hours
minutes = int( ( (userSeconds % 86400) % 3600) / 60) # Convert the remainder of the previous operation to minutes
seconds = int( ( ( (userSeconds % 86400) % 3600) % 60) ) # Convert the remainder of the previous operation to seconds

if userSeconds >= 0: # Verifies that user entered a number greater that 0
    print()
    print( userSeconds, 'seconds = ' + str(days) + ' day(s), ' + str(hours) + ' hour(s), '\
    + str(minutes) + ' minute(s), ' + str(seconds) + ' second(s).')
    print()

else: # Prints an error message if the number is lower than 0
    print()
    print('Error: The number you entered is lower that zero (0).' \
    '\n' 'Please restart the program and enter a number greater than zero (0).')