# This program converts pounds to kilograms
# Author: Regis Kouatcho, CCIS1505-51, Jerry Covington

# Get the number of pounds to convert from user
lbsweight = float(input('What is the weight in Pounds? '))

# Convert the weight to pounds
kgweight = lbsweight * 0.454

# Display the results
print('The weight in Kilograms is', format(kgweight, '.2f'))