# This program is a for loop that writes the numbers 1 to 10
# to for_loops.txt file

def main():
    # Open the loops.txt for writing
    loops = open('loops.txt', 'w')

    # Get each nomber in the range and write it in the loops.txt
    for count in range(1, 10, 2):
        loops.write( str(count) + '\n')
    
    # Close the file
    loops.close()

# Run the program
main()