#   Julie is very happy with the programs that you have written so far.
# Your next job is to write a program that she can use to modify the
# quantity field in an existing record. This will allow her to keep
# the records up to date as coffee is sold or more coffee of an
# existing type is added to inventory.
#   To modify a record in a sequential file, you must create a second
# temporary file. You copy all of the original file’s records to the
# temporary file, but when you get to the record that is to be modified,
# you do not write its old contents to the temporary file. Instead, you
# write its new modified values to the temporary file. Then, you finish
# copying any remaining records from the original file to the temporary
# file. 
#   The temporary file then takes the place of the original file.
# You delete the original file and rename the temporary file, giving
# it the name that the original file had on the computer’s disk.
# Here is the general algorithm for your program.
#   Open the original file for input and create a temporary
#   file for output.
#   Get the description of the record to be modified and the new value
#  for the quantity.
#   Read the first description field from the original file.
#   While the description field is not empty:
#       Read the quantity field.
#       If this record ’s description field matches the description
#       entered:
#           Write the new data to the temporary file.
#       Else:
#           Write the existing record to the temporary file.
#       Read the next description field.
#   Close the original file and the temporary file.
#   Delete the original file.
#   Rename the temporary file, giving it the name of the original file.
# 
# Notice at the end of the algorithm you delete the original file then
# rename the temporary file. The Python standard library’s os module
# provides a function named remove, that deletes a file on the disk.
# You simply pass the name of the file as an argument to the function.
# Here is an example of how you would delete a file named coffee.txt:
#   remove('coffee.txt')
# The os module also provides a function named rename, that renames a file.
# Here is an example of how you would use it to rename the file temp.txt
# to coffee.txt:
#   rename('temp.txt', 'coffee.txt')

# ######################################

# This program allows the user to modify the quantity in a record in 
# the coffee.txt file.

import os # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as a flag
    found = False

    # Get the search value and the new quantity
    searh = input('Enter a description to search for: ')
    new_qty = int( input('Enter the new quantity: '))

    # Open the original coffee.txt file.
    coffee_file = open('coffee.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the frist record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float( coffee_file.readline())

        # Strip the '\n\' from the description
        descr = descr.rstrip('\n')

        # Write either this record to the temporary file, or the new record
        # if this in one that is to be modified
        if descr == searh:
            # Write the modified record to the temp file
            temp_file.write(descr + '\n')
            temp_file.write( str(new_qty) + '\n')

            # Set thge found flag to True
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write( str(qty) + '\n')

        # Read the next description
        descr = coffee_file.readline()
    
    # Close the coffee file and the temporary file.
    coffee_file.close()
    temp_file.close()

    # Delete the original coffee.txt file.
    os.remove('coffee.txt')

    # Rename the temporary file
    os.rename('temp.txt', 'coffee.txt')

    # If the search value was not found in the file,
    # display a message
    if found:
        print('The file has been updated')
    else:
        print('That item was not found in the file')

# Call the main function
main()