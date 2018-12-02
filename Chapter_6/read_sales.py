# This program reads all of the values in the sales.txt file.

def main():
    # Open the sales.txt file for reading
    sales_file = open('sales.txt', 'r')

    # Read the first line form the file but don't convert
    # to a number yet. We still need to test for an empty 
    # string
    line = sales_file.readline()

    # As long as an empty line is not returned from readline
    # continue processing
    while line !='':
        amount = float(line) # convert line to a float
        print(format(amount, '.2f')) # Format and display the amount.

        # Read the next line.
        line = sales_file.readline()

    # Close the file
    sales_file.close()

# Call the main function
main()