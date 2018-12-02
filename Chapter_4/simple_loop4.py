# this program demonstrates how the range function can be used with a for loop.

# Print a message 5 times
for x in range(5):
    print('Hello World!')

# Passing two arguments to the range function. First value is the beginning and the second one is the end
print()
for y in range(1, 5):
    print(y)

# By default, sequence numbers are incread by one. If a third argument is added in the range function, it becomes a step value. 
# Instead of increaing by 1, each successive number will increase by the steo value.
print()
for num in range(1, 10, 2):
    print(num)