# Midnight Coffee Roasters, Inc. is a small company that imports raw 
# coffee beans from around the world and roasts them to create a 
# variety of gourmet coffees. Julie, the owner of the company, has 
# asked you to write a series of programs that she can use to manage her
# inventory. After speaking with her, you have determined that a file is
# needed to keep inventory records. Each record should have two fields
# to hold the following data:
#   • Description. A string containing the name of the coffee
#   • Quantity in inventory. The number of pounds in inventory, as a 
#       floating-point number
#
# Your first job is to write a program that can be used to add records 
# to the file. Program 6-15 shows the code. Note the output file is 
# opened in append mode. Each time the program is executed, the new 
# records will be added to the file’s existing contents.

##### Begin Program #####

# This program adds coffee inventory records to the coffee.txt file

def main():

    # Create a variable to control the loop
    another = 'y'

    # Open the coffee.txt file in append mode.
    coffee_file = open('coffee.txt', 'a')

    # Add records to the file.
    while another == 'y' or another == 'Y':
        
        # Get the coffee record data.
        print('Enter the following coffee data:')
        descr = input('Description: ')
        qty = int( input('Quantity (in pounds): '))

        # append the data to the file
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # Determine whether the user wants to add another record
        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ')

    
    # Close the file
    coffee_file.close()
    print('Data appended to coffee.txt')

# Call the main function
main()