# This programs uses the for loop to read all of the values in
# the sales.txt file.

def main():
    # Open the sales.txt file for reading
    sales_file = open('sales.txt', 'r')

    # Read all the lines from the file
    for line in sales_file:
        amount = float(line) # Convert line to a float
        print( format(amount, '.2f'))
    
    # Close the file
    sales_file.close()

# Call the main function
main()