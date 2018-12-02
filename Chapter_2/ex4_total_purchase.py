# This program calculate the total purchase of a user, including sales tax. Sales tax is 7 percent
# Author: Regis Kouatcho, CCIS1505-51, Jerry Covington

# Get the item price from the user
item1 = float(input('Enter the 1st item price '))
item2 = float(input('Enter the 2nd item price '))
item3 = float(input('Enter the 3rd item price '))
item4 = float(input('Enter the 4th item price '))
item5 = float(input('Enter the 5th item price '))

# Calculates the subtotal of the sale
subtotal = item1 + item2 + item3 + item4 + item5

# Calculates the sales tax amount
sales_tax = subtotal * 0.07

#Displays the sale subtotal
print('Your subtotal is: $', format(subtotal, '.2f'), sep='')
print('Tax amount: $', format(sales_tax, '.2f'), sep='')
print('The total purchase is $', format(subtotal + sales_tax, '.2f'), sep='')