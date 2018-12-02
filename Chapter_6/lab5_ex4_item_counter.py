# Exercice 4
# Assume that a file containing a series of names (as strings) is named
# names.txt and exists on the computer's disk. Write a program that 
# displays the number of names that are stored in it. Use a variable to
# keep a count of the number of items that are read from the file.)

def main():
    
    # Open the file names.txt
    names = open('names.txt', 'r')

    # Read the first item in the file
    item = names.readline()

    # Initialize the variable that will hold the number of names
    numberOfNames = 0

    # Initalize the while loop to verify that the value for item is not empty
    while item != "":
        numberOfNames = numberOfNames + 1
        item = names.readline()
    
    # Print the number of names in the names.txt file
    print()
    print('The file names.txt has', numberOfNames, 'name(s) in it.')
    print()

    # Close the names.txt file
    names.close()

# Call the main function
main()