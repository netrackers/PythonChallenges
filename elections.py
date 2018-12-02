# This program calculates the percentage of femal and males registered in a class.
# Author: Regis Kouatcho, CCIS1505-51, Jerry Covington


# Get the number of females
biya = int(input('Enter the number for Paul Biya:'))
garga = int(input('Enter the number for Garga Haman:'))
kamto = int(input('Enter the number for Kamto Maurice:'))
libii = int(input('Enter the number for Libii Cabral:'))
matomba = int(input('Enter the number for Matomba Serge:'))
# males = int(input('Enter the number of male students:'))

# Calculate the total number of students
total_students = 3524326

# Calculating the percentage of for each gender
males_percent = (biya/total_students) * 100
females_percent = (biya/total_students) * 100

# Displaying the results
print('Total number of students:', total_students)
print('Prcentage of females:', females_percent)
print('Percentage of males:', males_percent)
