# Assume a file containing a series of integers is named numbers.txt 
# and exists on the computer’s disk. Write a program that reads all of
# the numbers stored in the file and calculates their total.

def main():
   
    try: # Begin exception / error handling
        # Open the numbers.txt file.
        numbers = open('numbers.txt', 'r')
    
        # Initialize an accumulator
        total = 0.0

        # Read the values from the file and accumulate them
        for items in numbers:
            total = total + int(items)
        
        # Print the total
        print()
        print('The sum of the numbers in numbers.txt is', total)
        print()
        
        # Close the file
        numbers.close()
   
    except Exception as err:
        print()
        print(err)
        print()

# Call the main function
main()