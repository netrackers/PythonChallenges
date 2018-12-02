# Exercice 1: Assume a file containing a series of integers is named
# numbers.txt and exists on the computer’s disk. Write a program that
# displays all of the numbers in the file.

def main():
    
    # open the file
    infile = open('numbers.txt', 'r')

    # Read the file content
    numbers = infile.read()

    # Display the file content:
    print(numbers)

    # Close the file
    infile.close()

# Call the main function
main()
