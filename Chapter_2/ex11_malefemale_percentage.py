# This program calculates the percentage of femal and males registered in a class.
# Author: Regis Kouatcho, CCIS1505-51, Jerry Covington


# Get the number of females
females = int(input('Enter the number of female students:'))
males = int(input('Enter the number of male students:'))

# Calculate the total number of students
total_students = females + males

# Calculating the percentage of for each gender
males_percent = (males/total_students) * 100
females_percent = (females/total_students) * 100

# Displaying the results
print('Total number of students:', total_students)
print('Prcentage of females:', females_percent)
print('Percentage of males:', males_percent)
