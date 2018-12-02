# Draws the box with perspective from Exercise 15
# Author: Regis Kouatcho, CCIS1505-51, Jerry Covington

import turtle

# Create constant for the main box
BOX_UPPER_RIGHT_X = 100
BOX_UPPER_RIGHT_Y = 0
BOX_LOWER_RIGHT_X = 100
BOX_LOWER_RIGHT_Y = -100
BOX_LOWER_LEFT_X = 0
BOX_LOWER_LEFT_Y = -100
BOX_UPPER_LEFT_X = 0
BOX_UPPER_LEFT_Y = 0

# changing the background color
turtle.bgcolor('light sky blue')

# Seeting the fill color
turtle.fillcolor('white')

# Setting the pen size
turtle.pensize(5)

# Setting turtle animation speed
turtle.speed(3)

# Hiding the turtle
turtle.hideturtle()

# Drawing
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(135)
turtle.forward(280)
turtle.right(135)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.right(135)
turtle.forward(140)
turtle.right(45)
turtle.forward(100)
turtle.penup()
turtle.goto(BOX_UPPER_RIGHT_X, BOX_UPPER_RIGHT_Y)
turtle.left(45)
turtle.pendown()
turtle.forward(140)
turtle.penup()
turtle.goto(BOX_LOWER_RIGHT_X, BOX_LOWER_RIGHT_Y)
turtle.left(45)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.goto(BOX_UPPER_LEFT_X, BOX_UPPER_LEFT_Y)
turtle.pendown()
turtle.forward(97)
turtle.done()