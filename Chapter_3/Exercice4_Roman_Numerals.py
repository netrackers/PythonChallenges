# Exercie 4 - Roman Numerals

# Write a program that prompts the user to enter a number within the range of 1 through 10.
# The program should display the Roman numeral version of that number. If the number is
# outside the range of 1 through 10, the program should display an error message. The following
# table shows the Roman numerals for the numbers 1 through 10:
# Number    Roman Numeral
# 1         I
# 2         II
# 3         III
# 4         IV
# 5         V
# 6         VI
# 7         VII
# 8         VIII
# 9         IX
# 10        X

# Get a number from the user
print()
userInput = int( input(' Please enter a number between 1 and 10: '))
print()

# Check the conditions and output the corresponding results
if userInput == 1:
    print('The roman equivalent of ', userInput, ' is I.')
elif userInput == 2:
    print('The roman equivalent of ', userInput, ' is II.')
elif userInput == 3:
    print('The roman equivalent of ', userInput, ' is III.')
elif userInput == 4:
    print('The roman equivalent of ', userInput, ' is IV.')
elif userInput == 5:
    print('The roman equivalent of ', userInput, ' is V.')
elif userInput == 6:
    print('The roman equivalent of ', userInput, ' is VI.')
elif userInput == 7:
    print('The roman equivalent of ', userInput, ' is VII.')
elif userInput == 8:
    print('The roman equivalent of ', userInput, ' is VII.')
elif userInput == 9:
    print('The roman equivalent of ', userInput, ' is IX.')
elif userInput == 10:
    print('The roman equivalent of ', userInput, ' is 10.')

# Display an error message if the number entered is not in the 1-10 range.
else:
    print('The number you entered is not in the range 1-10. Please '+\
    'restart the program and try again')

