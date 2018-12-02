# Chapter 3 - Exercice 2: Areas of Rectangles
# The area of a rectangle is the rectangle’s length times its width. Write a program that asks
# for the length and width of two rectangles. The program should tell the user which rectangle
# has the greater area, or if the areas are the same.

# Get the measurement of the first rectangle and calcultate it's area.
print()
rectangle1Length = float( input( 'Please enter the length of the 1st rectangle: ') )
rectangle1Width = float( input( 'Please enter the width of the 1st rectangle: ') )
print('Rectangle 1 Length = ', rectangle1Length, \
' and Rectangle 1 width = ', rectangle1Width)
print( 'Rectangle 1 area = ', rectangle1Length * rectangle1Width)

# Get the measurements of the second rectable and calculte it's area.
print()
rectangle2Length = float( input( 'Please enter the length of the 2nd rectangle: ') )
rectangle2Width = float( input( 'Please enter the width of the 2nd rectangle: ') )
print('Rectangle 2 length = ', rectangle2Length, \
' and Rectangle 2 width = ', rectangle2Width)
print( 'Rectangle 2 area = ', rectangle2Length * rectangle2Width)
print()

# Calculating the area
rectangle1Area = rectangle1Length * rectangle1Width
rectangle2Area = rectangle2Length * rectangle2Width

# Comparing the areas and displaying the corresponding message.
if rectangle1Area > rectangle2Area:
    print ('Rectangle 1 is bigger than Rectangle 2 ')
elif rectangle1Area < rectangle2Area:
    print ('Rectangle 2 is bigger than Rectangle 1')
else: 
    print ('The 2 rectangles have the same area')
print()