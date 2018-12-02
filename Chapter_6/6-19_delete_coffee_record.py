# Your last task is to write a program that Julie can use to delete 
# records from the coffee.txt file. Like the process of modifying a 
# record, the process of deleting a record from a sequential access file
# requires that you create a second temporary file. You copy all of the
# original file’s records to the temporary file, except for the record
# that is to be deleted. The temporary file then takes the place of the
# original file. You delete the original file and rename the temporary 
# file, giving it the name that the original file had on the computer’s
# disk. Here is the general algorithm for your program.
#   - Open the original file for input and create a temporary file for output
#   - Get the description of the record to be deleted.
#   - Read the description field of the first record in the original file.
#   - While the description is not empty:
#       * Read the quantity field.
#       * If this record's description field does not match the description entered:
#           - Write the record to the temporary file.
#       * Read the next description field.
#   - Close the original file and the temporary file.
#   - Delete the original file.
#   - Rename the temporary file, giving it the name of the original file.

import os # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as flag
    found = False

    # Get the coffee to delete
    search = input( 'Which coffee do you want to delete? ')

    # Open the originial coffee.txt
    coffee_file = open('coffee.txt', 'r')

    # Open the temporary file
    temp_file =  open( 'temp.txt', 'w')

    # Read the first record's description field
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field
        qty = float( coffee_file.readline())

        # Strip the '\n' from the description
        descr = descr.rstrip('\n')

        # If this is not the record to delete, then write it to the temporary file
        if descr != search:
            # Write the record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write( str(qty) + '\n')
        else:
            # Set the found flag to True
            found = True
        
        # Read the next description.
        descr = coffee_file.readline()

    # Close the coffee file and the temporary file.
    coffee_file.close()
    temp_file.close()

    # Delete the original coffee.txt file.
    os.remove('coffee.txt')

    # Rename the temporary file
    os.rename('temp.txt', 'coffee.txt')

    # If the search value was not found in the file, display a message.
    if found:
        print('The file has been updated')
    else:
        print('That item was not found in the file')

# Call the main function
main()