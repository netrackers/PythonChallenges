# This program desmonstrates how numbers must be converted to strings
# before they are written to a text file.

def main():
    # Open a file for writing
    outfile = open('numbers.txt', 'w')

    # Get three numbers from user
    num1 = int( input ('Enter a number: '))
    num2 = int( input ('Enter a second number: '))
    num3 = int( input ('Enter a third number: '))

    # Write the numbers to the file
    outfile.write( str(num1) + '\n')
    outfile.write( str(num2) + '\n')
    outfile.write( str(num3) + '\n')

    # Close the file
    outfile.close()
    print('Data written to numbers.txt')

# Call the main function
main()
