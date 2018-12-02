# Draws a crosshair with the four directions from Exercice 15
# Author: Regis Kouatcho, CCIS1505-51, Jerry Covington

import turtle

# changing the background color
turtle.bgcolor('light sky blue')

# Set windows sixe
turtle.setup(500,600)

# Setting the pen size
turtle.pensize(2)

# Setting turtle animation speed
turtle.speed(3)

# Hiding the turtle
turtle.hideturtle()

# Create coordinates for the names locations
NORTH_X = 0
NORTH_Y = 150
SOUTH_X = 0
SOUTH_Y = -150
WEST_X = -150
WEST_Y = 0
EAST_X = 150
EAST_Y = 0

# Place the Names on the drawing
turtle.penup()
turtle.goto(NORTH_X, NORTH_Y)
turtle.write('North')
turtle.goto(SOUTH_X, SOUTH_Y)
turtle.write('South')
turtle.goto(WEST_X, WEST_Y)
turtle.write('West')
turtle.goto(EAST_X, EAST_Y)
turtle.write('East')
turtle.goto(10, -12)
turtle.pendown()
turtle.circle(20)
turtle.penup()
turtle.goto(10, 150)
turtle.pendown()
turtle.right(90)
turtle.forward(285)
turtle.penup()
turtle.goto(145,7)
turtle.right(90)
turtle.pendown()
turtle.forward(265)


turtle.done()
