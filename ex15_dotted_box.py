# This program draws a box with dots and lines
# Author: Regis Kouatcho, CCIS1505-51, Jerry Covington


import turtle

# Set windows size
turtle.setup(500,600)

# changing the background color
turtle.bgcolor('light sky blue')

# Setting turtle animation speed
turtle.speed(3)

# Hiding the turtle
turtle.hideturtle()

# Setting the pen size
turtle.pensize(2)

# Setup the turtle
turtle.penup()


# Create coordinates for the dots
UPPER_RIGHT_DOT_X = 150
UPPER_RIGHT_DOT_Y = 150
LOWER_RIGHT_DOT_X = 150
LOWER_RIGHT_DOT_Y = -150
UPPER_LEFT_DOT_X = -150
UPPER_LEFT_DOT_Y = 150
LOWER_LEFT_DOT_X = -150
LOWER_LEFT_DOT_Y = -150

# Place the dots on the drawing
turtle.dot(size=5)
turtle.goto(UPPER_RIGHT_DOT_X, UPPER_RIGHT_DOT_Y)
turtle.dot(size=5)
turtle.goto(UPPER_LEFT_DOT_X, UPPER_LEFT_DOT_Y)
turtle.dot(size=5)
turtle.goto(LOWER_LEFT_DOT_X, LOWER_LEFT_DOT_Y)
turtle.dot(size=5)
turtle.goto(LOWER_RIGHT_DOT_X, LOWER_RIGHT_DOT_Y)
turtle.dot(size=5)
turtle.left(90)
turtle.pendown()
turtle.goto(UPPER_RIGHT_DOT_X, UPPER_RIGHT_DOT_Y)
turtle.left(135)
turtle.goto(LOWER_LEFT_DOT_X, LOWER_LEFT_DOT_Y)
turtle.right(135)
turtle.goto(UPPER_LEFT_DOT_X, UPPER_LEFT_DOT_Y)
turtle.right(135)
turtle.goto(LOWER_RIGHT_DOT_X, LOWER_RIGHT_DOT_Y)
turtle.right(135)
turtle.forward(50)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(30)
turtle.penup()
turtle.goto(UPPER_RIGHT_DOT_X, UPPER_RIGHT_DOT_Y)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(30)

turtle.done()