# This program displays the contents of a file

def main():
    # Get the name of a file.
    filename = input('Enter a filename: ')

    try:
        # Open the file
        infile = open(filename, 'r')

        # Read the file's contents
        contents = infile.read()

        # Display the file's content
        print(contents)

        # Close the file.
        infile.close()
    
    except FileNotFoundError:
        print('An error occured trying to read the file', filename)

# Call the main function.
main()