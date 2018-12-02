# This program calls the split method using the '/' character as a 
# separator.

def main():
    # Get a date from the user
    date_string = input('Enter a date in the MM/DD/YYYY format: ')

    # Split the date
    date_list = date_string.split('/')

    # Display each pieve of the date
    print('Month:', date_list[0])
    print('Day:', date_list[1])
    print('Year:', date_list[2])

# Call the main function
main()