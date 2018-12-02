# This program demonstrates the repetition operator.

def main():
    # Print nine rows of increasing length.
    for count in range(1, 10):
        print('#' * count)
    
    # Print nine rows of decreasing length.
    for count in range(8, 0, -1):
        print('#' * count)

# Call the main function
main()